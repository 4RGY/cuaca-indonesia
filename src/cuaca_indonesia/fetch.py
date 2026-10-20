"""Ambil prakiraan cuaca BMKG per kelurahan.

Catatan operasional: endpoint `api.bmkg.go.id` dilindungi Cloudflare yang menolak
fingerprint TLS pustaka `requests` biasa (403), dan hanya menerima kode wilayah
format bertitik (`31.71.02.1001`), bukan 10 digit tanpa titik (502). Karena itu
proyek ini memakai `curl_cffi` dengan impersonasi browser dan selalu menormalkan
kode adm4 ke format bertitik.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from curl_cffi import requests

API = "https://api.bmkg.go.id/publik/prakiraan-cuaca"
JEDA_ANTAR_PERMINTAAN = 1.0  # detik, API BMKG membalas 502 kalau dipanggil rapat


def format_adm4(kode: str) -> str:
    """`3171021001` -> `31.71.02.1001` (format yang diterima API BMKG)."""
    bersih = "".join(ch for ch in str(kode) if ch.isalnum())
    if "." in str(kode):
        return kode
    if len(bersih) != 10:
        raise ValueError(f"kode adm4 harus 10 digit, dapat: {kode!r}")
    return f"{bersih[0:2]}.{bersih[2:4]}.{bersih[4:6]}.{bersih[6:]}"


def ambil_prakiraan(adm4: str, cache_dir: Path | None = None, retries: int = 4) -> dict[str, Any]:
    """GET prakiraan satu kelurahan, dengan cache lokal dan retry berjenjang."""
    kode = format_adm4(adm4)
    if cache_dir is not None:
        cache = cache_dir / f"{kode}.json"
        if cache.exists():
            try:
                return json.loads(cache.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                pass  # cache rusak, ambil ulang dari jaringan

    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            resp = requests.get(API, params={"adm4": kode}, impersonate="chrome", timeout=40)
            if resp.status_code == 200:
                data = resp.json()
                if cache_dir is not None:
                    cache_dir.mkdir(parents=True, exist_ok=True)
                    (cache_dir / f"{kode}.json").write_text(
                        json.dumps(data, ensure_ascii=False), encoding="utf-8"
                    )
                return data
            last_error = RuntimeError(f"HTTP {resp.status_code} untuk adm4 {kode}")
        except Exception as exc:  # noqa: BLE001 - curl_cffi punya hierarki error sendiri
            last_error = exc
        time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"gagal mengambil prakiraan {kode}: {last_error}")


def ambil_banyak(kota: dict[str, dict], cache_dir: Path | None = None) -> dict[str, dict]:
    """Ambil prakiraan untuk banyak kota. Kota yang gagal dilaporkan, tidak mematikan pipeline."""
    hasil: dict[str, dict] = {}
    for nama, info in kota.items():
        try:
            hasil[nama] = ambil_prakiraan(info["adm4"], cache_dir=cache_dir)
            print(f"      {nama:16s} ok")
        except RuntimeError as exc:
            print(f"      {nama:16s} GAGAL: {exc}")
        time.sleep(JEDA_ANTAR_PERMINTAAN)
    return hasil
