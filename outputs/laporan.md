# Prakiraan Cuaca Indonesia

Analisis 19 kota, 408 slot prakiraan 3 jam (5 Nov 2026 sampai 7 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-05 01:30 UTC.

## Angka kunci

- Paling basah: **Medan** dengan 15.7 mm dalam 63 jam.
- Paling kering: **Pekanbaru** dengan 0.2 mm.
- Suhu tertinggi: **Semarang** 36 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 16.0 C (selisih harian rata-rata 7.3 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Medan | 15.7 | 45 | 0 | 23-30 | 90 | 8.6 | Berawan |
| Palembang | 11.4 | 30 | 0 | 24-33 | 87 | 6.4 | Berawan |
| Pontianak | 9.7 | 42 | 0 | 23-32 | 90 | 10.3 | Cerah Berawan |
| Padang | 9.2 | 51 | 0 | 25-27 | 86 | 6.9 | Berawan |
| Manado | 8.2 | 33 | 0 | 23-32 | 83 | 7.5 | Cerah Berawan |
| Ambon | 7.0 | 27 | 0 | 24-30 | 89 | 11.2 | Cerah |
| Semarang | 5.7 | 30 | 0 | 25-36 | 70 | 11.6 | Cerah |
| Balikpapan | 5.1 | 42 | 0 | 25-30 | 82 | 13.3 | Cerah Berawan |
| Bandar Lampung | 4.6 | 36 | 0 | 24-31 | 81 | 13.9 | Cerah |
| Banda Aceh | 3.9 | 42 | 0 | 24-29 | 86 | 13.7 | Cerah Berawan |
| Jakarta Pusat | 3.4 | 42 | 0 | 26-32 | 75 | 12.1 | Cerah Berawan |
| Mataram | 2.6 | 30 | 0 | 24-31 | 79 | 12.5 | Cerah |
| Bandung | 2.2 | 18 | 0 | 20-30 | 76 | 9.4 | Berawan |
| Jayapura | 1.7 | 15 | 0 | 23-31 | 86 | 10.4 | Cerah Berawan |
| Kupang | 1.3 | 12 | 0 | 25-35 | 71 | 18.5 | Cerah |
| Surabaya | 0.5 | 15 | 0 | 26-36 | 62 | 24.8 | Cerah |
| Denpasar | 0.3 | 9 | 0 | 25-31 | 78 | 14.3 | Cerah |
| Makassar | 0.2 | 6 | 0 | 26-30 | 78 | 17.4 | Berawan |
| Pekanbaru | 0.2 | 6 | 0 | 24-31 | 88 | 7.7 | Cerah Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah Berawan | 128 | 31.4 | 19 |
| Cerah | 126 | 30.9 | 17 |
| Berawan | 97 | 23.8 | 15 |
| Udara Kabur | 26 | 6.4 | 7 |
| Hujan Ringan | 25 | 6.1 | 9 |
| Petir | 2 | 0.5 | 2 |
| Hujan Sedang | 2 | 0.5 | 2 |
| Hujan Petir | 1 | 0.2 | 1 |
| Kabut/Asap | 1 | 0.2 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Surabaya** 06 Nov 14:00: suhu 35 C (Cerah)
- **Surabaya** 05 Nov 14:00: suhu 35 C (Cerah)
- **Kupang** 05 Nov 13:00: suhu 35 C (Berawan)
- **Kupang** 06 Nov 13:00: suhu 34 C (Cerah)
- **Kupang** 05 Nov 16:00: suhu 34 C (Cerah Berawan)
- **Kupang** 06 Nov 16:00: suhu 34 C (Cerah)
- **Kupang** 07 Nov 13:00: suhu 35 C (Cerah)
- **Surabaya** 07 Nov 14:00: suhu 34 C (Cerah)
- **Semarang** 05 Nov 14:00: suhu 36 C (Cerah)
- **Semarang** 05 Nov 11:00: suhu 35 C (Cerah Berawan)
- **Surabaya** 05 Nov 11:00: suhu 36 C (Cerah)
- **Surabaya** 06 Nov 11:00: suhu 36 C (Cerah)

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
