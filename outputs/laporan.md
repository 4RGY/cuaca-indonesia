# Prakiraan Cuaca Indonesia

Analisis 19 kota, 408 slot prakiraan 3 jam (11 Nov 2026 sampai 13 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-11 01:18 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 18.2 mm dalam 63 jam.
- Paling kering: **Makassar** dengan 2.9 mm.
- Suhu tertinggi: **Kupang** 34 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 15.0 C (selisih harian rata-rata 6.7 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 18.2 | 30 | 0 | 19-28 | 83 | 18.4 | Berawan |
| Medan | 17.4 | 54 | 0 | 23-29 | 91 | 7.3 | Berawan |
| Pontianak | 14.0 | 39 | 0 | 24-30 | 93 | 10.4 | Berawan |
| Ambon | 11.5 | 33 | 0 | 24-32 | 86 | 13.0 | Hujan Ringan |
| Palembang | 11.3 | 51 | 0 | 24-32 | 87 | 8.0 | Udara Kabur |
| Semarang | 11.2 | 18 | 0 | 25-33 | 81 | 12.8 | Cerah |
| Manado | 9.9 | 24 | 0 | 24-33 | 84 | 7.3 | Cerah |
| Mataram | 9.6 | 36 | 0 | 24-32 | 87 | 27.8 | Cerah |
| Pekanbaru | 9.3 | 54 | 0 | 23-30 | 90 | 7.8 | Berawan |
| Padang | 8.6 | 60 | 0 | 25-27 | 85 | 6.0 | Berawan |
| Denpasar | 7.9 | 36 | 0 | 25-30 | 82 | 14.8 | Berawan |
| Banda Aceh | 6.7 | 48 | 0 | 24-29 | 88 | 12.9 | Berawan |
| Kupang | 6.0 | 21 | 0 | 25-34 | 71 | 27.8 | Cerah |
| Jakarta Pusat | 5.9 | 48 | 0 | 24-31 | 79 | 10.3 | Berawan |
| Balikpapan | 4.4 | 45 | 0 | 25-29 | 83 | 14.1 | Berawan |
| Bandar Lampung | 3.9 | 42 | 0 | 24-31 | 80 | 13.8 | Berawan |
| Surabaya | 3.8 | 30 | 0 | 25-34 | 74 | 18.5 | Berawan |
| Jayapura | 3.4 | 33 | 0 | 23-29 | 85 | 15.9 | Berawan |
| Makassar | 2.9 | 30 | 0 | 26-30 | 77 | 13.8 | Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 179 | 43.9 | 19 |
| Cerah | 81 | 19.9 | 14 |
| Cerah Berawan | 69 | 16.9 | 17 |
| Hujan Ringan | 58 | 14.2 | 15 |
| Udara Kabur | 16 | 3.9 | 5 |
| Petir | 5 | 1.2 | 3 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 12 Nov 13:00: suhu 34 C (Cerah)
- **Kupang** 13 Nov 13:00: suhu 34 C (Cerah)
- **Surabaya** 13 Nov 14:00: suhu 34 C (Cerah)
- **Surabaya** 13 Nov 11:00: suhu 34 C (Cerah)
- **Kupang** 13 Nov 10:00: suhu 34 C (Cerah Berawan)

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
