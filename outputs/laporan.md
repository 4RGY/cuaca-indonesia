# Prakiraan Cuaca Indonesia

Analisis 19 kota, 410 slot prakiraan 3 jam (8 Nov 2026 sampai 10 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-08 00:45 UTC.

## Angka kunci

- Paling basah: **Manado** dengan 17.6 mm dalam 66 jam.
- Paling kering: **Makassar** dengan 0.7 mm.
- Suhu tertinggi: **Surabaya** 36 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 16.0 C (selisih harian rata-rata 7.2 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Manado | 17.6 | 24 | 0 | 24-30 | 87 | 8.3 | Cerah Berawan |
| Bandung | 17.1 | 36 | 0 | 20-30 | 80 | 8.4 | Berawan |
| Banda Aceh | 15.0 | 51 | 0 | 24-29 | 88 | 8.1 | Berawan |
| Pontianak | 14.4 | 39 | 0 | 23-33 | 91 | 11.5 | Cerah Berawan |
| Pekanbaru | 12.2 | 54 | 0 | 24-31 | 89 | 10.4 | Berawan |
| Balikpapan | 11.6 | 54 | 0 | 25-29 | 85 | 14.8 | Berawan |
| Ambon | 11.2 | 30 | 0 | 23-29 | 87 | 10.7 | Cerah |
| Medan | 11.2 | 39 | 0 | 23-30 | 90 | 11.4 | Berawan |
| Padang | 9.4 | 51 | 0 | 25-28 | 85 | 6.4 | Berawan |
| Semarang | 6.9 | 54 | 0 | 24-35 | 77 | 13.6 | Cerah |
| Jakarta Pusat | 5.7 | 51 | 0 | 25-31 | 80 | 11.1 | Berawan |
| Mataram | 4.8 | 18 | 0 | 25-32 | 76 | 19.9 | Cerah |
| Bandar Lampung | 4.7 | 39 | 0 | 24-32 | 79 | 14.8 | Berawan |
| Denpasar | 4.2 | 42 | 0 | 25-33 | 81 | 15.9 | Cerah |
| Palembang | 3.8 | 33 | 0 | 25-32 | 83 | 9.4 | Berawan |
| Kupang | 2.1 | 21 | 0 | 26-33 | 75 | 27.8 | Cerah |
| Jayapura | 1.8 | 30 | 0 | 23-29 | 83 | 11.7 | Cerah |
| Surabaya | 1.4 | 6 | 0 | 24-36 | 68 | 13.0 | Cerah |
| Makassar | 0.7 | 18 | 0 | 26-32 | 74 | 13.6 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 144 | 35.1 | 17 |
| Berawan | 105 | 25.6 | 14 |
| Cerah Berawan | 82 | 20.0 | 19 |
| Hujan Ringan | 47 | 11.5 | 12 |
| Udara Kabur | 26 | 6.3 | 8 |
| Hujan Petir | 4 | 1.0 | 1 |
| Petir | 2 | 0.5 | 2 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Semarang** 08 Nov 14:00: suhu 35 C (Cerah Berawan)
- **Semarang** 08 Nov 11:00: suhu 34 C (Cerah)
- **Surabaya** 08 Nov 14:00: suhu 36 C (Cerah Berawan)
- **Semarang** 10 Nov 14:00: suhu 34 C (Cerah)
- **Surabaya** 09 Nov 14:00: suhu 35 C (Cerah)
- **Surabaya** 08 Nov 11:00: suhu 36 C (Cerah)
- **Surabaya** 10 Nov 14:00: suhu 34 C (Cerah)
- **Surabaya** 09 Nov 11:00: suhu 35 C (Cerah)

## Gambar

![total curah hujan 66 jam per kota](figures/01_curah_hujan_kota.png)

![peta panas curah hujan harian](figures/02_heatmap_harian.png)

![rentang suhu dan suhu terasa](figures/03_rentang_suhu.png)

![profil hujan kota terbasah](figures/04_profil_hujan_terbasah.png)

## Catatan metode

- Setiap slot mewakili 3 jam. `jam_hujan` = jumlah slot dengan curah hujan > 0 dikali 3.
- Suhu terasa memakai apparent temperature Steadman: `AT = Ta + 0.33e - 0.70ws - 4.00`, dengan `e` tekanan uap air dari suhu dan kelembapan.
- Kategori hujan per slot: kering (< 0,1 mm), ringan (< 5 mm), sedang (< 20 mm), lebat (< 50 mm), sangat lebat.
- Prakiraan BMKG adalah keluaran model, bukan observasi. Angka bisa berubah setiap kali pipeline dijalankan.
