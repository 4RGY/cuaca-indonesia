"""Grafik prakiraan cuaca. Gaya bersih, satu pesan per gambar."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

TINTA = "#1c2430"
ABU = "#6b7a8f"
GARIS = "#dfe5ec"
BIRU = "#1d4ed8"
AKSEN = "#0f766e"
AMBER = "#d97706"
MERAH = "#b3261e"

CMAP_HUJAN = "Blues"


def _gaya() -> None:
    plt.rcParams.update({
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": GARIS,
        "axes.labelcolor": TINTA,
        "axes.titlecolor": TINTA,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.labelsize": 10,
        "axes.grid": True,
        "grid.color": GARIS,
        "grid.linewidth": 0.7,
        "xtick.color": ABU,
        "ytick.color": ABU,
        "font.size": 9.5,
        "figure.dpi": 150,
        "savefig.bbox": "tight",
    })
    for spine in ("top", "right"):
        plt.rcParams[f"axes.spines.{spine}"] = False


def _simpan(fig: plt.Figure, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, facecolor="white")
    plt.close(fig)
    return path


def curah_hujan_per_kota(ringkas: pd.DataFrame, path: Path, horizon: int = 72) -> Path:
    _gaya()
    data = ringkas.sort_values("curah_total_mm")
    fig, ax = plt.subplots(figsize=(8.6, 5.4))
    warna = [MERAH if v >= 50 else AMBER if v >= 20 else AKSEN for v in data["curah_total_mm"]]
    ax.barh(data["kota"], data["curah_total_mm"], color=warna, height=0.68)
    for y, (nilai, jam) in enumerate(zip(data["curah_total_mm"], data["jam_hujan"])):
        ax.text(nilai + 0.6, y, f"{nilai:.1f} mm / {jam} jam", va="center", fontsize=8, color=ABU)
    ax.set_title(f"Total curah hujan {horizon} jam ke depan")
    ax.set_xlabel("Curah hujan (mm)")
    ax.set_xlim(0, max(data["curah_total_mm"].max() * 1.28, 5))
    return _simpan(fig, path)


def heatmap_harian(tabel: pd.DataFrame, path: Path) -> Path:
    _gaya()
    fig, ax = plt.subplots(figsize=(8.2, 6.4))
    data = tabel.loc[tabel.sum(axis=1).sort_values(ascending=False).index]
    im = ax.imshow(data.to_numpy(), aspect="auto", cmap=CMAP_HUJAN, vmin=0)
    ax.set_xticks(range(len(data.columns)), [str(c) for c in data.columns], fontsize=8.5)
    ax.set_yticks(range(len(data.index)), data.index, fontsize=8.5)
    ax.grid(False)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            nilai = data.iat[i, j]
            ax.text(j, i, f"{nilai:.1f}", ha="center", va="center", fontsize=7.5,
                    color="white" if nilai > data.to_numpy().max() * 0.55 else TINTA)
    ax.set_title("Curah hujan harian per kota (mm)")
    fig.colorbar(im, ax=ax, shrink=0.72, label="mm")
    for spine in ax.spines.values():
        spine.set_visible(False)
    return _simpan(fig, path)


def rentang_suhu(ringkas: pd.DataFrame, path: Path) -> Path:
    _gaya()
    data = ringkas.sort_values("suhu_maks")
    fig, ax = plt.subplots(figsize=(8.6, 5.4))
    y = range(len(data))
    ax.hlines(y, data["suhu_min"], data["suhu_maks"], color=GARIS, linewidth=5)
    ax.scatter(data["suhu_min"], y, color=BIRU, s=34, label="suhu terendah", zorder=3)
    ax.scatter(data["suhu_maks"], y, color=MERAH, s=34, label="suhu tertinggi", zorder=3)
    ax.scatter(data["suhu_terasa_maks"], y, color=AMBER, s=34, marker="D",
               label="terasa paling panas", zorder=3)
    ax.set_yticks(list(y), data["kota"], fontsize=8.5)
    ax.set_xlabel("Suhu (C)")
    ax.set_title("Rentang suhu prakiraan dan suhu terasa")
    ax.legend(frameon=False, fontsize=8.5, loc="lower right")
    return _simpan(fig, path)


def profil_hujan(df: pd.DataFrame, ringkas: pd.DataFrame, path: Path, n: int = 4) -> Path:
    _gaya()
    kota = list(ringkas.head(n)["kota"])
    fig, ax = plt.subplots(figsize=(9.4, 4.6))
    for nama in kota:
        data = df[df["kota"] == nama]
        ax.step(data["waktu_lokal"], data["curah_hujan_mm"], where="mid", linewidth=1.7, label=nama)
    ax.set_title("Profil curah hujan per slot 3 jam, kota terbasah")
    ax.set_ylabel("Curah hujan (mm/3 jam)")
    ax.set_xlabel("Waktu lokal (WIB/WITA/WIT sesuai kota)")
    ax.legend(frameon=False, fontsize=8.5, ncol=2)
    fig.autofmt_xdate(rotation=0, ha="center")
    return _simpan(fig, path)


def buat_semua(df: pd.DataFrame, ringkas: pd.DataFrame, tabel: pd.DataFrame, outdir: Path,
               horizon: int = 72) -> list[Path]:
    return [
        curah_hujan_per_kota(ringkas, outdir / "01_curah_hujan_kota.png", horizon=horizon),
        heatmap_harian(tabel, outdir / "02_heatmap_harian.png"),
        rentang_suhu(ringkas, outdir / "03_rentang_suhu.png"),
        profil_hujan(df, ringkas, outdir / "04_profil_hujan_terbasah.png"),
    ]
