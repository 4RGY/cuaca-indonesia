"""Laporan markdown cuaca Indonesia."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from . import analysis

BULAN = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]


def _tgl(nilai: Any) -> str:
    try:
        return f"{nilai.day} {BULAN[nilai.month - 1]} {nilai.year}"
    except AttributeError:
        return str(nilai)


def _jam(nilai: Any) -> str:
    try:
        return nilai.strftime("%d %b %H:%M")
    except AttributeError:
        return str(nilai)


def tabel_markdown(data: pd.DataFrame, kolom: list[str], judul: list[str]) -> str:
    garis = "| " + " | ".join(judul) + " |"
    pisah = "|" + "|".join(["---"] * len(judul)) + "|"
    isi = [
        "| " + " | ".join(f"{row[k]}" for k in kolom) + " |"
        for _, row in data.iterrows()
    ]
    return "\n".join([garis, pisah, *isi])


def blok_ringkasan(df: pd.DataFrame, ringkas: pd.DataFrame) -> dict[str, Any]:
    urut = analysis.peringkat(ringkas)
    return {
        "dibuat_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "periode_mulai": _tgl(df["waktu_lokal"].min()),
        "periode_selesai": _tgl(df["waktu_lokal"].max()),
        "horizon_jam": analysis.horizon_jam(df),
        "jumlah_kota": urut.get("jumlah_kota", 0),
        "jumlah_slot": int(len(df)),
        "terbasah": urut.get("terbasah"),
        "terkering": urut.get("terkering"),
        "terpanas": urut.get("terpanas"),
        "terdingin": urut.get("terdingin"),
        "kota_tanpa_hujan": urut.get("kota_tanpa_hujan"),
        "peringatan": len(analysis.peringatan(df)),
    }


def tulis_laporan(
    df: pd.DataFrame,
    ringkas: pd.DataFrame,
    tabel: pd.DataFrame,
    path: Path,
) -> dict[str, Any]:
    blok = blok_ringkasan(df, ringkas)
    peringatan = analysis.peringatan(df)
    kontras = analysis.kontras_suhu(ringkas)

    baris: list[str] = []
    baris.append("# Prakiraan Cuaca Indonesia")
    baris.append("")
    baris.append(
        f"Analisis {blok['jumlah_kota']} kota, {blok['jumlah_slot']} slot prakiraan 3 jam "
        f"({blok['periode_mulai']} sampai {blok['periode_selesai']}). "
        f"Sumber: API prakiraan cuaca BMKG. Dibuat {blok['dibuat_utc']}."
    )
    baris.append("")
    baris.append("## Angka kunci")
    baris.append("")
    terbasah_kota, terbasah_mm = blok["terbasah"]
    terkering_kota, terkering_mm = blok["terkering"]
    terpanas_kota, terpanas_c = blok["terpanas"]
    terdingin_kota, terdingin_c = blok["terdingin"]
    baris.append(f"- Paling basah: **{terbasah_kota}** dengan {terbasah_mm:.1f} mm dalam {blok['horizon_jam']} jam.")
    baris.append(f"- Paling kering: **{terkering_kota}** dengan {terkering_mm:.1f} mm.")
    baris.append(f"- Suhu tertinggi: **{terpanas_kota}** {terpanas_c:.0f} C.")
    baris.append(f"- Suhu terendah: **{terdingin_kota}** {terdingin_c:.0f} C.")
    baris.append(
        f"- Rentang suhu antar kota: {kontras['rentang_antar_kota_c']} C "
        f"(selisih harian rata-rata {kontras['selisih_harian_rata_rata_c']} C)."
    )
    baris.append(f"- Kota tanpa hujan sama sekali: {blok['kota_tanpa_hujan']} dari {blok['jumlah_kota']}.")
    baris.append("")

    baris.append("## Ringkasan per kota")
    baris.append("")
    saji = ringkas.copy()
    saji["kelembapan_rata"] = saji["kelembapan_rata"].round(0).astype(int)
    saji["suhu"] = saji.apply(lambda r: f"{r['suhu_min']:.0f}-{r['suhu_maks']:.0f}", axis=1)
    saji["curah"] = saji["curah_total_mm"].map(lambda v: f"{v:.1f}")
    baris.append(tabel_markdown(
        saji[["kota", "curah", "jam_hujan", "slot_lebat", "suhu", "kelembapan_rata",
              "angin_maks", "kondisi_dominan"]],
        ["kota", "curah", "jam_hujan", "slot_lebat", "suhu", "kelembapan_rata",
         "angin_maks", "kondisi_dominan"],
        ["Kota", f"Hujan {blok['horizon_jam']} jam (mm)", "Jam hujan", "Slot lebat", "Suhu (C)",
         "RH (%)", "Angin maks (km/jam)", "Kondisi dominan"],
    ))
    baris.append("")

    kondisi = analysis.ringkasan_kondisi(df)
    baris.append("## Kondisi yang diprediksi")
    baris.append("")
    baris.append(tabel_markdown(
        kondisi[["kondisi", "slot", "persen", "kota"]],
        ["kondisi", "slot", "persen", "kota"],
        ["Kondisi", "Slot", "Porsi (%)", "Jumlah kota"],
    ))
    baris.append("")

    baris.append("## Peringatan dini")
    baris.append("")
    if peringatan:
        baris.append(
            "Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang "
            "(>= 30 km/jam), atau suhu ekstrem (>= 34 C):"
        )
        baris.append("")
        for item in peringatan:
            baris.append(
                f"- **{item['kota']}** {_jam(item['waktu'])}: {item['alasan']} ({item['kondisi']})"
            )
    else:
        baris.append("Tidak ada slot yang melewati ambang pada horizon prakiraan ini.")
    baris.append("")

    baris.append("## Gambar")
    baris.append("")
    for nama, ket in [
        ("01_curah_hujan_kota.png", f"total curah hujan {blok['horizon_jam']} jam per kota"),
        ("02_heatmap_harian.png", "peta panas curah hujan harian"),
        ("03_rentang_suhu.png", "rentang suhu dan suhu terasa"),
        ("04_profil_hujan_terbasah.png", "profil hujan kota terbasah"),
    ]:
        baris.append(f"![{ket}](figures/{nama})")
        baris.append("")

    baris.append("## Catatan metode")
    baris.append("")
    baris.append(
        "- Setiap slot mewakili 3 jam. `jam_hujan` = jumlah slot dengan curah hujan > 0 dikali 3."
    )
    baris.append(
        "- Suhu terasa memakai apparent temperature Steadman: "
        "`AT = Ta + 0.33e - 0.70ws - 4.00`, dengan `e` tekanan uap air dari suhu dan kelembapan."
    )
    baris.append(
        "- Kategori hujan per slot: kering (< 0,1 mm), ringan (< 5 mm), sedang (< 20 mm), "
        "lebat (< 50 mm), sangat lebat."
    )
    baris.append(
        "- Prakiraan BMKG adalah keluaran model, bukan observasi. Angka bisa berubah setiap "
        "kali pipeline dijalankan."
    )
    baris.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(baris), encoding="utf-8")
    return blok
