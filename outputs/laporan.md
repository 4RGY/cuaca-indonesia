# Prakiraan Cuaca Indonesia

Analisis 19 kota, 388 slot prakiraan 3 jam (25 Nov 2026 sampai 27 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-25 04:18 UTC.

## Angka kunci

- Paling basah: **Medan** dengan 26.5 mm dalam 60 jam.
- Paling kering: **Ambon** dengan 0.0 mm.
- Suhu tertinggi: **Semarang** 36 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 16.0 C (selisih harian rata-rata 6.7 C).
- Kota tanpa hujan sama sekali: 1 dari 19.

## Ringkasan per kota

| Kota | Hujan 60 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Medan | 26.5 | 45 | 0 | 24-32 | 92 | 12.4 | Hujan Ringan |
| Padang | 26.2 | 63 | 0 | 25-27 | 88 | 6.5 | Hujan Ringan |
| Kupang | 25.3 | 48 | 0 | 25-34 | 83 | 22.2 | Hujan Ringan |
| Palembang | 24.9 | 60 | 0 | 24-30 | 91 | 5.9 | Berawan |
| Bandung | 24.3 | 39 | 0 | 20-26 | 90 | 7.5 | Berawan |
| Pontianak | 19.3 | 57 | 0 | 24-33 | 92 | 11.6 | Cerah Berawan |
| Semarang | 17.2 | 45 | 0 | 25-36 | 85 | 18.5 | Berawan |
| Jakarta Pusat | 14.2 | 57 | 0 | 25-31 | 86 | 7.4 | Berawan |
| Bandar Lampung | 11.8 | 33 | 0 | 24-30 | 86 | 16.3 | Berawan |
| Pekanbaru | 11.5 | 54 | 0 | 24-31 | 90 | 8.4 | Berawan |
| Mataram | 11.1 | 42 | 0 | 24-30 | 87 | 14.8 | Cerah |
| Surabaya | 8.6 | 48 | 0 | 25-34 | 80 | 9.7 | Berawan |
| Manado | 8.5 | 39 | 0 | 23-31 | 86 | 7.5 | Cerah Berawan |
| Denpasar | 8.0 | 21 | 0 | 26-32 | 85 | 27.8 | Berawan |
| Balikpapan | 6.8 | 42 | 0 | 24-29 | 86 | 12.7 | Berawan |
| Jayapura | 6.1 | 45 | 0 | 24-27 | 90 | 14.5 | Berawan |
| Banda Aceh | 5.4 | 45 | 0 | 24-29 | 87 | 15.2 | Berawan |
| Makassar | 1.6 | 6 | 0 | 26-34 | 82 | 13.2 | Cerah |
| Ambon | 0.0 | 0 | 0 | 24-32 | 84 | 12.4 | Cerah Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 156 | 40.2 | 19 |
| Hujan Ringan | 91 | 23.5 | 17 |
| Cerah Berawan | 73 | 18.8 | 16 |
| Cerah | 49 | 12.6 | 12 |
| Udara Kabur | 14 | 3.6 | 7 |
| Hujan Petir | 4 | 1.0 | 3 |
| Hujan Sedang | 1 | 0.3 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 25 Nov 13:00: suhu 34 C (Hujan Ringan)
- **Kupang** 26 Nov 13:00: suhu 34 C (Hujan Ringan)
- **Kupang** 27 Nov 13:00: suhu 34 C (Hujan Petir)
- **Semarang** 27 Nov 11:00: suhu 36 C (Berawan)
- **Semarang** 25 Nov 11:00: suhu 34 C (Berawan)
- **Makassar** 25 Nov 13:00: suhu 34 C (Cerah Berawan)
- **Makassar** 26 Nov 13:00: suhu 34 C (Hujan Ringan)
- **Surabaya** 26 Nov 12:00: suhu 34 C (Berawan)
- **Makassar** 27 Nov 13:00: suhu 34 C (Cerah Berawan)

## Gambar

![total curah hujan 60 jam per kota](figures/01_curah_hujan_kota.png)

![peta panas curah hujan harian](figures/02_heatmap_harian.png)

![rentang suhu dan suhu terasa](figures/03_rentang_suhu.png)

![profil hujan kota terbasah](figures/04_profil_hujan_terbasah.png)

## Catatan metode

- Setiap slot mewakili 3 jam. `jam_hujan` = jumlah slot dengan curah hujan > 0 dikali 3.
- Suhu terasa memakai apparent temperature Steadman: `AT = Ta + 0.33e - 0.70ws - 4.00`, dengan `e` tekanan uap air dari suhu dan kelembapan.
- Kategori hujan per slot: kering (< 0,1 mm), ringan (< 5 mm), sedang (< 20 mm), lebat (< 50 mm), sangat lebat.
- Prakiraan BMKG adalah keluaran model, bukan observasi. Angka bisa berubah setiap kali pipeline dijalankan.
