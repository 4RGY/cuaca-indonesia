"""Tes tanpa jaringan: parsing payload BMKG dan agregasi."""

from __future__ import annotations

from datetime import datetime, timedelta

import pandas as pd
import pytest

from cuaca_indonesia import analysis, fetch, parse


def _slot(waktu: datetime, suhu: float = 30.0, hujan: float = 0.0, angin: float = 10.0,
          lembap: int = 80) -> dict:
    return {
        "local_datetime": waktu.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_datetime": waktu.strftime("%Y-%m-%d %H:%M:%S"),
        "t": suhu,
        "hu": lembap,
        "tp": hujan,
        "tcc": 60,
        "ws": angin,
        "wd": "Timur",
        "weather_desc": "Hujan Ringan" if hujan > 0 else "Cerah Berawan",
    }


def _payload(kota: str = "Jakarta Pusat", n_hari: int = 2) -> dict:
    awal = datetime(2026, 10, 21, 7, 0)
    hari = []
    for h in range(n_hari):
        hari.append([
            _slot(awal + timedelta(hours=3 * i + 24 * h), hujan=2.5 if i % 4 == 0 else 0.0)
            for i in range(8)
        ])
    return {
        "lokasi": {
            "adm4": "31.71.01.1001",
            "provinsi": "DKI Jakarta",
            "kotkab": "Kota Adm. Jakarta Pusat",
            "kecamatan": "Gambir",
            "desa": "Gambir",
        },
        "data": [{"lokasi": {}, "cuaca": hari}],
    }


def test_format_adm4():
    assert fetch.format_adm4("3171021001") == "31.71.02.1001"
    assert fetch.format_adm4("31.71.02.1001") == "31.71.02.1001"
    with pytest.raises(ValueError):
        fetch.format_adm4("3171")


def test_flatten_membuka_slot_bertingkat():
    baris = parse.flatten(_payload(), "Jakarta Pusat")
    assert len(baris) == 16
    assert baris[0]["kota"] == "Jakarta Pusat"
    assert baris[0]["provinsi"] == "DKI Jakarta"
    assert isinstance(baris[0]["waktu_lokal"], datetime)


def test_suhu_terasa_lebih_panas_saat_lembap():
    kering = parse.suhu_terasa(32.0, 40, 10)
    lembap = parse.suhu_terasa(32.0, 95, 10)
    assert lembap > kering
    assert lembap > 32.0  # udara lembap bikin terasa lebih panas


def test_suhu_terasa_turun_saat_angin_kencang():
    tenang = parse.suhu_terasa(30.0, 70, 0)
    berangin = parse.suhu_terasa(30.0, 70, 40)
    assert berangin < tenang


@pytest.mark.parametrize("mm,label", [
    (0.0, "kering"), (0.2, "ringan"), (4.9, "ringan"),
    (5.0, "sedang"), (19.9, "sedang"), (20.0, "lebat"),
    (49.9, "lebat"), (50.0, "sangat lebat"),
])
def test_kategori_hujan(mm, label):
    assert parse.kategori_hujan(mm) == label


def test_dataframe_memotong_horizon():
    df = parse.build_dataframe({"Jakarta Pusat": _payload(n_hari=3)}, horizon_jam=24)
    assert df["kota"].nunique() == 1
    assert df["waktu_lokal"].max() < df["waktu_lokal"].min() + timedelta(hours=24)
    assert len(df) == 8


def test_ringkasan_dan_peringatan():
    payload = {
        "Jakarta Pusat": _payload(),
        "Kupang": _payload(kota="Kupang"),
    }
    # buat satu slot hujan lebat di Kupang
    payload["Kupang"]["data"][0]["cuaca"][0][1]["tp"] = 25.0
    df = parse.build_dataframe(payload, horizon_jam=48)
    ringkas = analysis.ringkasan_kota(df)

    assert len(ringkas) == 2
    assert ringkas.iloc[0]["kota"] == "Kupang"  # paling basah di urutan pertama
    assert (ringkas["jam_hujan"] == ringkas["slot_hujan"] * 3).all()

    peringatan = analysis.peringatan(df)
    assert peringatan
    assert peringatan[0]["kota"] == "Kupang"
    assert "25.0 mm" in peringatan[0]["alasan"]


def test_harian_pivot():
    df = parse.build_dataframe({"Jakarta Pusat": _payload(n_hari=2)}, horizon_jam=48)
    tabel = analysis.harian(df)
    assert tabel.index.tolist() == ["Jakarta Pusat"]
    assert tabel.shape[1] >= 1
    assert tabel.iloc[0].sum() == pytest.approx(df["curah_hujan_mm"].sum(), rel=1e-6)


def test_kontras_suhu():
    payload = {"Jakarta Pusat": _payload(), "Kupang": _payload(kota="Kupang")}
    df = parse.build_dataframe(payload, horizon_jam=24)
    df.loc[df["kota"] == "Kupang", "suhu_c"] = 35.0
    kontras = analysis.kontras_suhu(analysis.ringkasan_kota(df))
    assert kontras["suhu_maks_tertinggi_c"] == 35.0
    assert kontras["rentang_antar_kota_c"] > 0
