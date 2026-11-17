# Prakiraan Cuaca Indonesia

Analisis 19 kota, 391 slot prakiraan 3 jam (17 Nov 2026 sampai 19 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-17 03:59 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 34.9 mm dalam 63 jam.
- Paling kering: **Ambon** dengan 0.0 mm.
- Suhu tertinggi: **Surabaya** 34 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 15.0 C (selisih harian rata-rata 6.5 C).
- Kota tanpa hujan sama sekali: 1 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 34.9 | 45 | 0 | 19-28 | 86 | 9.4 | Berawan |
| Medan | 29.2 | 60 | 0 | 23-29 | 90 | 9.0 | Hujan Ringan |
| Padang | 28.5 | 54 | 0 | 25-28 | 84 | 7.7 | Hujan Ringan |
| Palembang | 23.9 | 51 | 0 | 24-30 | 89 | 7.2 | Berawan |
| Pontianak | 23.1 | 57 | 0 | 24-32 | 92 | 10.3 | Hujan Ringan |
| Mataram | 19.8 | 30 | 0 | 25-32 | 88 | 27.8 | Berawan |
| Jakarta Pusat | 16.5 | 51 | 0 | 24-32 | 83 | 8.0 | Berawan |
| Semarang | 16.3 | 33 | 0 | 25-33 | 83 | 9.5 | Berawan |
| Surabaya | 11.5 | 42 | 0 | 25-34 | 79 | 37.2 | Berawan |
| Pekanbaru | 10.8 | 54 | 0 | 24-30 | 89 | 9.9 | Berawan |
| Kupang | 10.4 | 33 | 0 | 26-34 | 80 | 27.8 | Cerah |
| Bandar Lampung | 10.4 | 39 | 0 | 24-31 | 84 | 14.0 | Cerah Berawan |
| Manado | 8.6 | 39 | 0 | 24-31 | 85 | 7.7 | Berawan |
| Balikpapan | 6.6 | 48 | 0 | 25-29 | 86 | 15.2 | Berawan |
| Banda Aceh | 5.0 | 30 | 0 | 24-30 | 86 | 12.3 | Berawan |
| Makassar | 4.7 | 30 | 0 | 25-30 | 83 | 8.9 | Berawan |
| Denpasar | 4.0 | 12 | 0 | 25-30 | 85 | 11.3 | Berawan |
| Jayapura | 1.4 | 3 | 0 | 24-29 | 85 | 11.8 | Cerah Berawan |
| Ambon | 0.0 | 0 | 0 | 24-30 | 88 | 11.6 | Cerah Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 145 | 37.1 | 19 |
| Hujan Ringan | 84 | 21.5 | 16 |
| Cerah Berawan | 78 | 19.9 | 15 |
| Cerah | 56 | 14.3 | 15 |
| Udara Kabur | 13 | 3.3 | 6 |
| Hujan Petir | 8 | 2.0 | 6 |
| Hujan Sedang | 4 | 1.0 | 3 |
| Petir | 3 | 0.8 | 3 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Surabaya** 18 Nov 14:00: angin 37 km/jam (Hujan Ringan)
- **Surabaya** 19 Nov 14:00: angin 36 km/jam (Hujan Ringan)
- **Surabaya** 17 Nov 14:00: angin 33 km/jam (Hujan Ringan)
- **Surabaya** 19 Nov 11:00: angin 36 km/jam (Cerah Berawan)
- **Kupang** 18 Nov 15:00: suhu 34 C (Hujan Petir)
- **Surabaya** 17 Nov 11:00: suhu 34 C (Berawan)

## Gambar

![total curah hujan 63 jam per kota](figures/01_curah_hujan_kota.png)

![peta panas curah hujan harian](figures/02_heatmap_harian.png)

![rentang suhu dan suhu terasa](figures/03_rentang_suhu.png)

![profil hujan kota terbasah](figures/04_profil_hujan_terbasah.png)

## Catatan metode

- Setiap slot mewakili 3 jam. `jam_hujan` = jumlah slot dengan curah hujan > 0 dikali 3.
- Suhu terasa memakai apparent temperature Steadman: `AT = Ta + 0.33e - 0.70ws - 4.00`, dengan `e` tekanan uap air dari suhu dan kelembapan.
- Kategori hujan per slot: kering (< 0,1 mm), ringan (< 5 mm), sedang (< 20 mm), lebat (< 50 mm), sangat lebat.
- Prakiraan BMKG adalah keluaran model, bukan observasi. Angka bisa berubah setiap kali pipeline dijalankan.
