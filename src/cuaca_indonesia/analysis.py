"""Agregasi prakiraan per kota dan penyusunan peringatan cuaca."""

from __future__ import annotations

from typing import Any

import pandas as pd

AMBANG_HUJAN_LEBAT_MM = 20.0   # per slot 3 jam
AMBANG_ANGIN_KENCANG_KMH = 30.0
AMBANG_PANAS_C = 34.0


def ringkasan_kota(df: pd.DataFrame) -> pd.DataFrame:
    """Satu baris per kota untuk seluruh horizon prakiraan."""
    def kondisi_dominan(series: pd.Series) -> str:
        bersih = series.dropna()
        return str(bersih.mode().iloc[0]) if not bersih.empty else "-"

    grup = df.groupby("kota", as_index=False).agg(
        provinsi=("provinsi", "first"),
        kecamatan=("kecamatan", "first"),
        curah_total_mm=("curah_hujan_mm", "sum"),
        slot_hujan=("curah_hujan_mm", lambda s: int((s > 0).sum())),
        slot_lebat=("curah_hujan_mm", lambda s: int((s >= AMBANG_HUJAN_LEBAT_MM).sum())),
        suhu_maks=("suhu_c", "max"),
        suhu_min=("suhu_c", "min"),
        suhu_terasa_maks=("suhu_terasa_c", "max"),
        kelembapan_rata=("kelembapan", "mean"),
        angin_maks=("angin_kmh", "max"),
        kondisi_dominan=("kondisi", kondisi_dominan),
        jumlah_slot=("curah_hujan_mm", "size"),
    )
    grup["jam_hujan"] = grup["slot_hujan"] * 3
    grup["curah_total_mm"] = grup["curah_total_mm"].round(1)
    grup["kelembapan_rata"] = grup["kelembapan_rata"].round(0)
    grup["selisih_suhu"] = (grup["suhu_maks"] - grup["suhu_min"]).round(1)
    return grup.sort_values("curah_total_mm", ascending=False).reset_index(drop=True)


def harian(df: pd.DataFrame) -> pd.DataFrame:
    """Total curah hujan per kota per tanggal."""
    tabel = df.pivot_table(
        index="kota", columns="tanggal", values="curah_hujan_mm", aggfunc="sum"
    ).fillna(0.0)
    return tabel.round(1)


def peringatan(df: pd.DataFrame) -> list[dict[str, Any]]:
    """Slot prakiraan yang melewati ambang hujan lebat, angin kencang, atau panas."""
    baris = df[
        (df["curah_hujan_mm"] >= AMBANG_HUJAN_LEBAT_MM)
        | (df["angin_kmh"] >= AMBANG_ANGIN_KENCANG_KMH)
        | (df["suhu_c"] >= AMBANG_PANAS_C)
    ].copy()
    if baris.empty:
        return []
    baris["skor"] = (
        baris["curah_hujan_mm"] / AMBANG_HUJAN_LEBAT_MM
        + baris["angin_kmh"] / AMBANG_ANGIN_KENCANG_KMH
    )
    baris = baris.sort_values(["skor", "curah_hujan_mm"], ascending=False)
    hasil = []
    for _, row in baris.head(12).iterrows():
        alasan = []
        if row["curah_hujan_mm"] >= AMBANG_HUJAN_LEBAT_MM:
            alasan.append(f"hujan {row['curah_hujan_mm']:.1f} mm/3 jam")
        if row["angin_kmh"] >= AMBANG_ANGIN_KENCANG_KMH:
            alasan.append(f"angin {row['angin_kmh']:.0f} km/jam")
        if row["suhu_c"] >= AMBANG_PANAS_C:
            alasan.append(f"suhu {row['suhu_c']:.0f} C")
        hasil.append({
            "kota": row["kota"],
            "waktu": row["waktu_lokal"],
            "kondisi": row["kondisi"],
            "alasan": ", ".join(alasan),
        })
    return hasil


def ringkasan_kondisi(df: pd.DataFrame) -> pd.DataFrame:
    """Sebaran kondisi cuaca yang diprediksi BMKG, dihitung per slot."""
    tabel = df.groupby("kondisi", as_index=False).agg(
        slot=("kondisi", "size"),
        kota=("kota", "nunique"),
    )
    tabel["persen"] = (tabel["slot"] / tabel["slot"].sum() * 100).round(1)
    return tabel.sort_values("slot", ascending=False).reset_index(drop=True)


def horizon_jam(df: pd.DataFrame) -> int:
    """Panjang horizon efektif (jam), dihitung dari slot median per kota."""
    per_kota = df.groupby("kota").size()
    return int(round(per_kota.median() * 3))


def peringkat(ringkas: pd.DataFrame) -> dict[str, Any]:
    if ringkas.empty:
        return {}
    terbasah = ringkas.iloc[0]
    terkering = ringkas.iloc[-1]
    terpanas = ringkas.loc[ringkas["suhu_maks"].idxmax()]
    terdingin = ringkas.loc[ringkas["suhu_min"].idxmin()]
    terangin = ringkas.loc[ringkas["angin_maks"].idxmax()]
    return {
        "terbasah": (terbasah["kota"], float(terbasah["curah_total_mm"])),
        "terkering": (terkering["kota"], float(terkering["curah_total_mm"])),
        "terpanas": (terpanas["kota"], float(terpanas["suhu_maks"])),
        "terdingin": (terdingin["kota"], float(terdingin["suhu_min"])),
        "terangin": (terangin["kota"], float(terangin["angin_maks"])),
        "kota_tanpa_hujan": int((ringkas["curah_total_mm"] <= 0).sum()),
        "jumlah_kota": int(len(ringkas)),
    }


def kontras_suhu(ringkas: pd.DataFrame) -> dict[str, Any]:
    if ringkas.empty:
        return {}
    return {
        "suhu_maks_tertinggi_c": float(ringkas["suhu_maks"].max()),
        "suhu_min_terendah_c": float(ringkas["suhu_min"].min()),
        "rentang_antar_kota_c": round(float(ringkas["suhu_maks"].max() - ringkas["suhu_min"].min()), 1),
        "selisih_harian_rata_rata_c": round(float(ringkas["selisih_suhu"].mean()), 1),
    }
