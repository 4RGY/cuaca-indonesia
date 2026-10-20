"""CLI: satu perintah untuk mengambil prakiraan, menghitung, dan menulis laporan."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import analysis, charts, fetch, parse, report

AKAR = Path(__file__).resolve().parents[2]


def muat_kota(path: Path) -> dict[str, dict]:
    if not path.exists():
        raise SystemExit(
            f"{path} belum ada. Jalankan dulu: python scripts/resolve_wilayah.py"
        )
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Analisis prakiraan cuaca BMKG multi-kota")
    parser.add_argument("--kota", type=Path, default=AKAR / "data" / "kota.json")
    parser.add_argument("--outdir", type=Path, default=AKAR / "outputs")
    parser.add_argument("--cache", type=Path, default=AKAR / "data" / "cache")
    parser.add_argument("--horizon", type=int, default=72, help="horizon prakiraan (jam)")
    parser.add_argument("--tanpa-cache", action="store_true", help="paksa ambil ulang dari BMKG")
    args = parser.parse_args(argv)

    kota = muat_kota(args.kota)
    cache = None if args.tanpa_cache else args.cache

    print(f"[1/4] ambil prakiraan {len(kota)} kota dari BMKG ...")
    payloads = fetch.ambil_banyak(kota, cache_dir=Path(cache) if cache else None)
    if not payloads:
        print("tidak ada data yang berhasil diambil", file=sys.stderr)
        return 1

    print("[2/4] rapikan data ...")
    df = parse.build_dataframe(payloads, horizon_jam=args.horizon)
    if df.empty:
        print("dataframe kosong setelah parsing", file=sys.stderr)
        return 1
    ringkas = analysis.ringkasan_kota(df)
    tabel = analysis.harian(df)

    args.outdir.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.outdir / "prakiraan.csv", index=False)
    ringkas.to_csv(args.outdir / "ringkasan_kota.csv", index=False)

    print("[3/4] gambar ...")
    horizon = analysis.horizon_jam(df)
    for path in charts.buat_semua(df, ringkas, tabel, args.outdir / "figures", horizon=horizon):
        print(f"      {path.relative_to(args.outdir)}")

    print("[4/4] tulis laporan ...")
    blok = report.tulis_laporan(df, ringkas, tabel, args.outdir / "laporan.md")
    (args.outdir / "ringkasan.json").write_text(
        json.dumps(blok, ensure_ascii=False, indent=2, default=str), encoding="utf-8"
    )

    print("\n== ringkas ==")
    print(f"kota        : {blok['jumlah_kota']}")
    print(f"slot 3 jam  : {blok['jumlah_slot']}")
    print(f"terbasah    : {blok['terbasah'][0]} ({blok['terbasah'][1]:.1f} mm)")
    print(f"terkering   : {blok['terkering'][0]} ({blok['terkering'][1]:.1f} mm)")
    print(f"terpanas    : {blok['terpanas'][0]} ({blok['terpanas'][1]:.0f} C)")
    print(f"peringatan  : {blok['peringatan']} slot")
    print(f"laporan     : {args.outdir / 'laporan.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
