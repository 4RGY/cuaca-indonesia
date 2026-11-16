# Prakiraan Cuaca Indonesia

Analisis 19 kota, 409 slot prakiraan 3 jam (16 Nov 2026 sampai 18 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-16 01:06 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 29.7 mm dalam 66 jam.
- Paling kering: **Jayapura** dengan 1.5 mm.
- Suhu tertinggi: **Surabaya** 35 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 16.0 C (selisih harian rata-rata 6.8 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 29.7 | 39 | 0 | 19-28 | 87 | 10.2 | Hujan Ringan |
| Padang | 20.9 | 60 | 0 | 25-28 | 86 | 7.5 | Hujan Ringan |
| Medan | 17.4 | 63 | 0 | 24-30 | 91 | 7.9 | Berawan |
| Pekanbaru | 15.3 | 30 | 0 | 23-29 | 90 | 10.4 | Hujan Ringan |
| Pontianak | 15.0 | 51 | 0 | 24-31 | 93 | 12.3 | Berawan |
| Palembang | 12.5 | 48 | 0 | 24-30 | 89 | 8.5 | Berawan |
| Semarang | 11.9 | 42 | 0 | 25-32 | 82 | 12.1 | Cerah Berawan |
| Manado | 10.6 | 36 | 0 | 25-32 | 83 | 9.8 | Cerah |
| Ambon | 9.7 | 27 | 0 | 24-31 | 90 | 10.3 | Cerah |
| Jakarta Pusat | 9.5 | 42 | 0 | 25-32 | 82 | 7.8 | Berawan |
| Kupang | 8.7 | 42 | 0 | 25-31 | 81 | 11.6 | Cerah |
| Bandar Lampung | 8.2 | 33 | 0 | 24-34 | 82 | 14.5 | Berawan |
| Balikpapan | 7.0 | 42 | 0 | 24-30 | 84 | 15.1 | Berawan |
| Surabaya | 6.7 | 39 | 0 | 25-35 | 79 | 13.9 | Cerah |
| Denpasar | 6.4 | 45 | 0 | 25-34 | 85 | 27.8 | Cerah Berawan |
| Makassar | 5.5 | 33 | 0 | 26-30 | 80 | 9.8 | Berawan |
| Mataram | 5.3 | 42 | 0 | 24-32 | 86 | 24.3 | Cerah Berawan |
| Banda Aceh | 2.8 | 18 | 0 | 24-30 | 85 | 7.7 | Cerah Berawan |
| Jayapura | 1.5 | 18 | 0 | 24-29 | 86 | 13.0 | Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 140 | 34.2 | 18 |
| Cerah Berawan | 98 | 24.0 | 18 |
| Hujan Ringan | 78 | 19.1 | 18 |
| Cerah | 77 | 18.8 | 15 |
| Udara Kabur | 10 | 2.4 | 7 |
| Hujan Petir | 3 | 0.7 | 2 |
| Petir | 2 | 0.5 | 2 |
| Hujan Sedang | 1 | 0.2 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Denpasar** 18 Nov 15:00: suhu 34 C (Cerah Berawan)
- **Denpasar** 16 Nov 12:00: suhu 34 C (Berawan)
- **Surabaya** 16 Nov 11:00: suhu 35 C (Cerah Berawan)
- **Surabaya** 17 Nov 11:00: suhu 34 C (Hujan Ringan)
- **Bandar Lampung** 16 Nov 12:00: suhu 34 C (Cerah Berawan)

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
