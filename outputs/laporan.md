# Prakiraan Cuaca Indonesia

Analisis 19 kota, 399 slot prakiraan 3 jam (19 Nov 2026 sampai 21 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-19 02:39 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 34.3 mm dalam 63 jam.
- Paling kering: **Padang** dengan 0.7 mm.
- Suhu tertinggi: **Semarang** 34 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 14.0 C (selisih harian rata-rata 6.6 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 34.3 | 30 | 0 | 20-28 | 89 | 8.1 | Hujan Ringan |
| Medan | 24.3 | 42 | 0 | 23-31 | 89 | 8.5 | Hujan Ringan |
| Pontianak | 19.2 | 48 | 0 | 24-31 | 91 | 13.0 | Berawan |
| Manado | 18.3 | 33 | 0 | 24-30 | 89 | 8.2 | Berawan |
| Semarang | 17.3 | 39 | 0 | 25-34 | 85 | 18.5 | Cerah |
| Pekanbaru | 16.8 | 27 | 0 | 24-30 | 87 | 8.0 | Berawan |
| Denpasar | 13.4 | 18 | 0 | 24-32 | 85 | 18.8 | Cerah Berawan |
| Banda Aceh | 12.5 | 45 | 0 | 24-30 | 87 | 14.1 | Berawan |
| Jakarta Pusat | 11.1 | 51 | 0 | 25-30 | 86 | 7.7 | Berawan |
| Palembang | 11.0 | 39 | 0 | 24-30 | 90 | 8.1 | Berawan |
| Ambon | 9.2 | 24 | 0 | 23-33 | 86 | 11.0 | Cerah |
| Mataram | 9.1 | 45 | 0 | 25-30 | 89 | 18.9 | Cerah |
| Surabaya | 7.5 | 51 | 0 | 25-34 | 82 | 39.6 | Cerah |
| Bandar Lampung | 7.5 | 42 | 0 | 24-30 | 88 | 11.3 | Berawan |
| Balikpapan | 7.3 | 21 | 0 | 25-29 | 85 | 17.6 | Berawan |
| Makassar | 6.7 | 24 | 0 | 26-30 | 84 | 10.7 | Berawan |
| Jayapura | 5.7 | 51 | 0 | 23-29 | 89 | 11.1 | Cerah Berawan |
| Kupang | 4.3 | 24 | 0 | 26-34 | 76 | 11.5 | Cerah |
| Padang | 0.7 | 15 | 0 | 25-29 | 79 | 8.6 | Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 140 | 35.1 | 18 |
| Cerah Berawan | 96 | 24.1 | 19 |
| Cerah | 78 | 19.5 | 16 |
| Hujan Ringan | 67 | 16.8 | 17 |
| Udara Kabur | 8 | 2.0 | 4 |
| Hujan Petir | 5 | 1.3 | 4 |
| Hujan Sedang | 4 | 1.0 | 3 |
| Petir | 1 | 0.3 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Surabaya** 19 Nov 12:00: angin 40 km/jam, suhu 34 C (Cerah Berawan)
- **Surabaya** 20 Nov 12:00: angin 37 km/jam (Cerah Berawan)
- **Surabaya** 21 Nov 15:00: angin 34 km/jam (Cerah)
- **Surabaya** 21 Nov 12:00: angin 34 km/jam (Cerah)
- **Semarang** 19 Nov 13:00: suhu 34 C (Hujan Ringan)
- **Semarang** 20 Nov 13:00: suhu 34 C (Hujan Ringan)
- **Semarang** 21 Nov 13:00: suhu 34 C (Cerah Berawan)
- **Kupang** 20 Nov 14:00: suhu 34 C (Cerah)
- **Kupang** 19 Nov 14:00: suhu 34 C (Cerah)
- **Kupang** 21 Nov 14:00: suhu 34 C (Berawan)

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
