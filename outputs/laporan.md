# Prakiraan Cuaca Indonesia

Analisis 19 kota, 338 slot prakiraan 3 jam (25 Okt 2026 sampai 27 Okt 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-10-24 23:22 UTC.

## Angka kunci

- Paling basah: **Pekanbaru** dengan 15.2 mm dalam 51 jam.
- Paling kering: **Surabaya** dengan 0.0 mm.
- Suhu tertinggi: **Surabaya** 35 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 16.0 C (selisih harian rata-rata 7.1 C).
- Kota tanpa hujan sama sekali: 3 dari 19.

## Ringkasan per kota

| Kota | Hujan 51 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Pekanbaru | 15.2 | 48 | 0 | 24-31 | 91 | 9.1 | Udara Kabur |
| Bandung | 14.7 | 33 | 0 | 19-27 | 89 | 6.7 | Berawan |
| Banda Aceh | 9.2 | 27 | 0 | 24-30 | 85 | 18.3 | Berawan |
| Pontianak | 9.1 | 36 | 0 | 23-33 | 92 | 9.2 | Udara Kabur |
| Medan | 7.6 | 42 | 0 | 23-30 | 91 | 6.3 | Berawan |
| Padang | 4.7 | 27 | 0 | 25-27 | 84 | 7.1 | Udara Kabur |
| Ambon | 4.5 | 30 | 0 | 24-30 | 89 | 8.3 | Udara Kabur |
| Semarang | 4.2 | 24 | 0 | 25-33 | 74 | 10.2 | Berawan |
| Balikpapan | 3.4 | 33 | 0 | 24-30 | 84 | 12.8 | Udara Kabur |
| Palembang | 3.3 | 24 | 0 | 24-32 | 86 | 10.7 | Udara Kabur |
| Jakarta Pusat | 3.2 | 36 | 0 | 25-31 | 81 | 10.5 | Berawan |
| Makassar | 2.6 | 27 | 0 | 25-29 | 82 | 14.9 | Berawan |
| Jayapura | 2.4 | 27 | 0 | 23-28 | 87 | 10.6 | Udara Kabur |
| Bandar Lampung | 1.9 | 18 | 0 | 24-31 | 77 | 19.5 | Berawan |
| Kupang | 0.6 | 9 | 0 | 24-32 | 70 | 16.5 | Berawan |
| Manado | 0.1 | 3 | 0 | 24-34 | 76 | 9.9 | Udara Kabur |
| Denpasar | 0.0 | 0 | 0 | 26-33 | 82 | 20.9 | Berawan |
| Mataram | 0.0 | 0 | 0 | 24-32 | 81 | 11.7 | Berawan |
| Surabaya | 0.0 | 0 | 0 | 24-35 | 66 | 13.1 | Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 135 | 39.9 | 15 |
| Udara Kabur | 118 | 34.9 | 10 |
| Cerah | 32 | 9.5 | 10 |
| Cerah Berawan | 30 | 8.9 | 12 |
| Hujan Ringan | 22 | 6.5 | 8 |
| Hujan Petir | 1 | 0.3 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Surabaya** 25 Oct 12:00: suhu 35 C (Berawan)
- **Surabaya** 25 Oct 15:00: suhu 34 C (Berawan)
- **Surabaya** 26 Oct 12:00: suhu 34 C (Berawan)
- **Manado** 26 Oct 16:00: suhu 34 C (Cerah)

## Gambar

![total curah hujan 51 jam per kota](figures/01_curah_hujan_kota.png)

![peta panas curah hujan harian](figures/02_heatmap_harian.png)

![rentang suhu dan suhu terasa](figures/03_rentang_suhu.png)

![profil hujan kota terbasah](figures/04_profil_hujan_terbasah.png)

## Catatan metode

- Setiap slot mewakili 3 jam. `jam_hujan` = jumlah slot dengan curah hujan > 0 dikali 3.
- Suhu terasa memakai apparent temperature Steadman: `AT = Ta + 0.33e - 0.70ws - 4.00`, dengan `e` tekanan uap air dari suhu dan kelembapan.
- Kategori hujan per slot: kering (< 0,1 mm), ringan (< 5 mm), sedang (< 20 mm), lebat (< 50 mm), sangat lebat.
- Prakiraan BMKG adalah keluaran model, bukan observasi. Angka bisa berubah setiap kali pipeline dijalankan.
