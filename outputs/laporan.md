# Prakiraan Cuaca Indonesia

Analisis 19 kota, 410 slot prakiraan 3 jam (15 Nov 2026 sampai 17 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-15 01:06 UTC.

## Angka kunci

- Paling basah: **Medan** dengan 41.2 mm dalam 66 jam.
- Paling kering: **Makassar** dengan 3.5 mm.
- Suhu tertinggi: **Surabaya** 36 C.
- Suhu terendah: **Bandung** 18 C.
- Rentang suhu antar kota: 18.0 C (selisih harian rata-rata 7.0 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Medan | 41.2 | 63 | 0 | 23-30 | 91 | 8.2 | Hujan Ringan |
| Bandung | 29.6 | 36 | 0 | 18-30 | 88 | 7.1 | Berawan |
| Pontianak | 19.3 | 57 | 0 | 23-30 | 93 | 11.9 | Berawan |
| Palembang | 16.5 | 33 | 0 | 24-34 | 88 | 9.2 | Berawan |
| Banda Aceh | 15.6 | 51 | 0 | 24-29 | 88 | 13.8 | Berawan |
| Padang | 15.2 | 57 | 0 | 25-28 | 85 | 6.0 | Berawan |
| Semarang | 13.8 | 42 | 0 | 25-32 | 82 | 12.2 | Berawan |
| Pekanbaru | 12.5 | 60 | 0 | 24-30 | 90 | 9.7 | Berawan |
| Bandar Lampung | 11.9 | 33 | 0 | 24-32 | 85 | 11.3 | Berawan |
| Mataram | 10.6 | 42 | 0 | 24-33 | 86 | 27.8 | Berawan |
| Ambon | 8.7 | 33 | 0 | 24-29 | 91 | 10.2 | Berawan |
| Manado | 8.3 | 33 | 0 | 25-30 | 85 | 9.7 | Cerah Berawan |
| Jakarta Pusat | 7.0 | 48 | 0 | 26-32 | 79 | 9.8 | Berawan |
| Surabaya | 6.6 | 42 | 0 | 25-36 | 77 | 13.2 | Cerah |
| Jayapura | 6.4 | 27 | 0 | 23-29 | 86 | 10.1 | Cerah Berawan |
| Balikpapan | 5.8 | 51 | 0 | 24-29 | 86 | 14.5 | Berawan |
| Denpasar | 5.5 | 42 | 0 | 25-34 | 84 | 13.9 | Berawan |
| Kupang | 4.8 | 36 | 0 | 26-34 | 79 | 27.8 | Cerah |
| Makassar | 3.5 | 48 | 0 | 26-30 | 81 | 11.9 | Cerah Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 140 | 34.1 | 19 |
| Cerah Berawan | 78 | 19.0 | 17 |
| Cerah | 75 | 18.3 | 18 |
| Hujan Ringan | 75 | 18.3 | 17 |
| Udara Kabur | 34 | 8.3 | 10 |
| Hujan Petir | 5 | 1.2 | 3 |
| Hujan Sedang | 3 | 0.7 | 2 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 16 Nov 13:00: suhu 34 C (Udara Kabur)
- **Denpasar** 15 Nov 15:00: suhu 34 C (Berawan)
- **Denpasar** 16 Nov 15:00: suhu 34 C (Cerah Berawan)
- **Palembang** 16 Nov 14:00: suhu 34 C (Hujan Ringan)
- **Palembang** 15 Nov 14:00: suhu 34 C (Hujan Ringan)
- **Surabaya** 15 Nov 14:00: suhu 36 C (Berawan)
- **Surabaya** 16 Nov 11:00: suhu 34 C (Cerah)
- **Surabaya** 15 Nov 11:00: suhu 36 C (Berawan)

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
