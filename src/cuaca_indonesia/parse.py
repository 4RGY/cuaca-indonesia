"""Normalisasi payload prakiraan BMKG jadi tabel panjang yang siap dianalisis."""

from __future__ import annotations

import math
from datetime import datetime, timedelta
from typing import Any

import pandas as pd

KOLOM = [
    "kota", "provinsi", "kecamatan", "desa", "adm4", "waktu_lokal",
    "suhu_c", "kelembapan", "curah_hujan_mm", "tutupan_awan",
    "angin_kmh", "arah_angin", "kondisi", "suhu_terasa_c",
]

# Kategori curah hujan per slot 3 jam (mm), mengikuti batas BMKG untuk durasi pendek.
BATAS_HUJAN = [(0.0, "kering"), (5.0, "ringan"), (20.0, "sedang"), (50.0, "lebat")]


def suhu_terasa(suhu_c: float, kelembapan: float, angin_kmh: float) -> float:
    """Apparent temperature Steadman (1984), versi operasional BoM.

    AT = Ta + 0.33 e - 0.70 ws - 4.00, dengan e = tekanan uap air (hPa)
    dan ws = kecepatan angin dalam m/s.
    """
    rh = max(1.0, min(100.0, float(kelembapan)))
    ws = max(0.0, float(angin_kmh) / 3.6)
    e = (rh / 100.0) * 6.105 * math.exp(17.27 * suhu_c / (237.7 + suhu_c))
    return round(suhu_c + 0.33 * e - 0.70 * ws - 4.00, 1)


def kategori_hujan(mm: float | None) -> str:
    if mm is None or mm <= 0:
        return "kering"
    for batas, label in BATAS_HUJAN[1:]:
        if mm < batas:
            return label
    return "sangat lebat"


def _slot_harian(cuaca: Any) -> list[dict[str, Any]]:
    """Payload BMKG menaruh slot per hari dalam list bertingkat."""
    if isinstance(cuaca, dict):
        return [cuaca]
    hasil: list[dict[str, Any]] = []
    for item in cuaca or []:
        if isinstance(item, list):
            hasil.extend(x for x in item if isinstance(x, dict))
        elif isinstance(item, dict):
            hasil.append(item)
    return hasil


def flatten(payload: dict[str, Any], kota: str) -> list[dict[str, Any]]:
    baris: list[dict[str, Any]] = []
    for grup in payload.get("data") or []:
        lokasi = grup.get("lokasi") or payload.get("lokasi") or {}
        for slot in _slot_harian(grup.get("cuaca")):
            waktu = slot.get("local_datetime") or slot.get("utc_datetime")
            if not waktu:
                continue
            suhu = slot.get("t")
            lembap = slot.get("hu")
            angin = slot.get("ws")
            hujan = slot.get("tp") or 0.0
            terasa = (
                suhu_terasa(float(suhu), float(lembap), float(angin))
                if suhu is not None and lembap is not None and angin is not None
                else None
            )
            baris.append({
                "kota": kota,
                "provinsi": lokasi.get("provinsi"),
                "kecamatan": lokasi.get("kecamatan"),
                "desa": lokasi.get("desa"),
                "adm4": lokasi.get("adm4"),
                "waktu_lokal": datetime.fromisoformat(str(waktu)),
                "suhu_c": suhu,
                "kelembapan": lembap,
                "curah_hujan_mm": float(hujan),
                "tutupan_awan": slot.get("tcc"),
                "angin_kmh": angin,
                "arah_angin": slot.get("wd"),
                "kondisi": slot.get("weather_desc"),
                "suhu_terasa_c": terasa,
            })
    return baris


def build_dataframe(payloads: dict[str, dict], horizon_jam: int = 72) -> pd.DataFrame:
    baris: list[dict[str, Any]] = []
    for kota, payload in payloads.items():
        baris.extend(flatten(payload, kota))
    df = pd.DataFrame(baris, columns=KOLOM)
    if df.empty:
        return df
    df = df.drop_duplicates(subset=["kota", "waktu_lokal"]).sort_values(["kota", "waktu_lokal"])
    awal = df.groupby("kota")["waktu_lokal"].transform("min")
    df = df[df["waktu_lokal"] < awal + timedelta(hours=horizon_jam)]
    df["kategori_hujan"] = df["curah_hujan_mm"].map(kategori_hujan)
    df["tanggal"] = df["waktu_lokal"].dt.date
    return df.reset_index(drop=True)
