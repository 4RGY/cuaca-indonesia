# Prakiraan Cuaca Indonesia

Analisis 19 kota, 399 slot prakiraan 3 jam (13 Nov 2026 sampai 15 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-13 01:55 UTC.

## Angka kunci

- Paling basah: **Medan** dengan 38.2 mm dalam 63 jam.
- Paling kering: **Denpasar** dengan 0.4 mm.
- Suhu tertinggi: **Surabaya** 36 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 16.0 C (selisih harian rata-rata 6.7 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Medan | 38.2 | 57 | 0 | 23-30 | 90 | 12.9 | Hujan Ringan |
| Banda Aceh | 19.1 | 51 | 0 | 24-28 | 91 | 9.1 | Hujan Ringan |
| Semarang | 17.1 | 36 | 0 | 25-34 | 79 | 18.5 | Cerah |
| Bandung | 16.0 | 24 | 0 | 20-32 | 83 | 8.6 | Berawan |
| Pontianak | 14.7 | 45 | 0 | 24-31 | 91 | 9.3 | Cerah Berawan |
| Palembang | 14.1 | 54 | 0 | 24-30 | 90 | 6.4 | Berawan |
| Padang | 11.8 | 57 | 0 | 25-27 | 86 | 6.2 | Berawan |
| Jakarta Pusat | 11.4 | 45 | 0 | 26-32 | 82 | 11.5 | Berawan |
| Mataram | 10.5 | 30 | 0 | 25-34 | 79 | 27.8 | Cerah |
| Ambon | 9.3 | 30 | 0 | 24-30 | 89 | 12.5 | Berawan |
| Pekanbaru | 8.7 | 36 | 0 | 24-30 | 90 | 8.4 | Berawan |
| Bandar Lampung | 8.4 | 51 | 0 | 24-31 | 86 | 9.0 | Berawan |
| Balikpapan | 4.9 | 39 | 0 | 26-30 | 83 | 17.1 | Berawan |
| Manado | 4.2 | 33 | 0 | 25-30 | 83 | 6.3 | Cerah |
| Surabaya | 3.6 | 21 | 0 | 26-36 | 69 | 27.8 | Berawan |
| Makassar | 3.5 | 36 | 0 | 27-31 | 79 | 13.0 | Cerah |
| Jayapura | 2.3 | 36 | 0 | 23-32 | 87 | 11.7 | Cerah Berawan |
| Kupang | 1.9 | 18 | 0 | 25-33 | 67 | 33.3 | Cerah |
| Denpasar | 0.4 | 6 | 0 | 26-33 | 81 | 23.8 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 132 | 33.1 | 17 |
| Cerah | 100 | 25.1 | 17 |
| Cerah Berawan | 84 | 21.1 | 18 |
| Hujan Ringan | 71 | 17.8 | 14 |
| Udara Kabur | 11 | 2.8 | 5 |
| Hujan Petir | 1 | 0.3 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 13 Nov 16:00: angin 33 km/jam (Cerah Berawan)
- **Mataram** 13 Nov 13:00: suhu 34 C (Hujan Ringan)
- **Kupang** 13 Nov 13:00: angin 32 km/jam (Cerah)
- **Kupang** 14 Nov 19:00: angin 32 km/jam (Cerah)
- **Surabaya** 13 Nov 12:00: suhu 36 C (Cerah)
- **Surabaya** 14 Nov 12:00: suhu 35 C (Cerah)
- **Semarang** 14 Nov 12:00: suhu 34 C (Cerah Berawan)
- **Semarang** 15 Nov 12:00: suhu 34 C (Cerah)
- **Semarang** 13 Nov 12:00: suhu 34 C (Cerah)
- **Surabaya** 15 Nov 12:00: suhu 34 C (Berawan)
- **Surabaya** 15 Nov 15:00: suhu 34 C (Cerah)
- **Surabaya** 13 Nov 15:00: suhu 34 C (Berawan)

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
