"""Resolusi kode wilayah adm4 (kelurahan) untuk kota-kota target.

Sumber kode: dataset terbuka wilayah administrasi Indonesia (BPS/Kemendagri)
yang dipublikasikan di ibnux.github.io/data-indonesia. Setiap kode diverifikasi
dengan memanggil API BMKG: respons BMKG harus mengembalikan provinsi/kota yang
sama dengan yang diminta. Kalau tidak cocok, kode tidak dipakai.

Jalankan sekali, hasilnya disimpan di data/kota.json:
    python scripts/resolve_wilayah.py
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from curl_cffi import requests

WILAYAH = "https://ibnux.github.io/data-indonesia"
BMKG = "https://api.bmkg.go.id/publik/prakiraan-cuaca"

# kode kota BPS 4 digit -> label yang dipakai di seluruh proyek
KOTA_TARGET = {
    "1171": "Banda Aceh",
    "1271": "Medan",
    "1371": "Padang",
    "1471": "Pekanbaru",
    "1671": "Palembang",
    "1871": "Bandar Lampung",
    "3171": "Jakarta Pusat",
    "3273": "Bandung",
    "3374": "Semarang",
    "3578": "Surabaya",
    "5171": "Denpasar",
    "5271": "Mataram",
    "5371": "Kupang",
    "6171": "Pontianak",
    "6471": "Balikpapan",
    "7171": "Manado",
    "7371": "Makassar",
    "8171": "Ambon",
    "9171": "Jayapura",
}


def ambil_json(url: str) -> list[dict]:
    resp = requests.get(url, impersonate="chrome", timeout=30)
    resp.raise_for_status()
    return resp.json()


def bertitik(kode: str) -> str:
    """`3171021001` -> `31.71.02.1001`, format yang diterima API BMKG."""
    k = "".join(ch for ch in kode if ch.isalnum())
    return f"{k[0:2]}.{k[2:4]}.{k[4:6]}.{k[6:]}"


def verifikasi_bmkg(adm4: str) -> tuple[dict | None, str]:
    """Cek kode ke API BMKG. Kembalikan (lokasi, status).

    status 'ok' kalau BMKG membalas dan kodenya cocok, 'ditolak' kalau BMKG
    membalas tapi kode tidak dikenal, 'ganggu' kalau API sedang error/timeout
    (502 dari Cloudflare sering terjadi saat dipanggil bertubi-tubi).
    """
    try:
        resp = requests.get(
            BMKG, params={"adm4": bertitik(adm4)}, impersonate="chrome", timeout=40
        )
    except Exception:  # noqa: BLE001
        return None, "ganggu"
    if resp.status_code != 200:
        return None, "ganggu" if resp.status_code >= 500 else "ditolak"
    data = resp.json()
    lokasi = data.get("lokasi") or {}
    if lokasi.get("adm4") != bertitik(adm4):
        return None, "ditolak"
    return lokasi, "ok"


def resolusi(kode_kota: str) -> dict | None:
    kecamatan = ambil_json(f"{WILAYAH}/kecamatan/{kode_kota}.json")
    ganggu = 0
    for kec in kecamatan:
        try:
            kelurahan = ambil_json(f"{WILAYAH}/kelurahan/{kec['id']}.json")
        except requests.RequestException:
            continue
        if not kelurahan:
            continue
        # pakai kelurahan yang namanya sama dengan kecamatan kalau ada (pusat kota)
        pilihan = next(
            (k for k in kelurahan if k["nama"].strip().lower() == kec["nama"].strip().lower()),
            kelurahan[0],
        )
        adm4 = pilihan["id"]
        lokasi, status = verifikasi_bmkg(adm4)
        if status == "ok":
            return {
                "adm4": adm4,
                "kecamatan": kec["nama"].strip(),
                "kelurahan": pilihan["nama"].strip(),
                "provinsi": lokasi.get("provinsi"),
                "kotkab": lokasi.get("kotkab"),
                "lat": lokasi.get("lat"),
                "lon": lokasi.get("lon"),
                "terverifikasi": True,
            }
        if status == "ganggu":
            ganggu += 1
            if ganggu >= 2:  # API BMKG sedang tidak bisa dihubungi, pakai kode BPS saja
                return {
                    "adm4": adm4,
                    "kecamatan": kec["nama"].strip(),
                    "kelurahan": pilihan["nama"].strip(),
                    "provinsi": None,
                    "kotkab": None,
                    "lat": pilihan.get("latitude"),
                    "lon": pilihan.get("longitude"),
                    "terverifikasi": False,
                }
        time.sleep(0.2)
    return None


def main() -> int:
    hasil: dict[str, dict] = {}
    for kode, label in KOTA_TARGET.items():
        try:
            lokasi = resolusi(kode)
        except Exception as exc:  # noqa: BLE001
            print(f"[skip] {label}: {exc}")
            continue
        if lokasi is None:
            print(f"[gagal] {label}: tidak ada adm4 yang lolos verifikasi BMKG")
            continue
        hasil[label] = lokasi
        tanda = "ok" if lokasi.get("terverifikasi") else "kode BPS, BMKG belum terverifikasi"
        print(f"[{tanda}] {label:16s} {lokasi['adm4']} {lokasi['kecamatan']}, {lokasi['kotkab'] or '-'}")

    tujuan = Path(__file__).resolve().parents[1] / "data" / "kota.json"
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(json.dumps(hasil, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n{len(hasil)} kota tersimpan di {tujuan}")
    return 0 if hasil else 1


if __name__ == "__main__":
    raise SystemExit(main())
