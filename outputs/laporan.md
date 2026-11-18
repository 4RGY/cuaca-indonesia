# Prakiraan Cuaca Indonesia

Analisis 19 kota, 397 slot prakiraan 3 jam (18 Nov 2026 sampai 20 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-18 02:57 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 53.5 mm dalam 63 jam.
- Paling kering: **Jayapura** dengan 3.6 mm.
- Suhu tertinggi: **Surabaya** 34 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 15.0 C (selisih harian rata-rata 6.8 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 53.5 | 45 | 0 | 19-27 | 89 | 46.2 | Hujan Ringan |
| Pontianak | 24.2 | 57 | 0 | 24-30 | 92 | 10.0 | Cerah Berawan |
| Medan | 22.3 | 42 | 0 | 24-29 | 89 | 8.7 | Berawan |
| Pekanbaru | 21.4 | 36 | 0 | 24-31 | 89 | 9.5 | Hujan Ringan |
| Semarang | 18.6 | 39 | 0 | 25-32 | 86 | 10.9 | Cerah Berawan |
| Manado | 17.6 | 42 | 0 | 24-30 | 88 | 10.1 | Berawan |
| Mataram | 16.4 | 30 | 0 | 24-33 | 82 | 18.5 | Hujan Ringan |
| Padang | 14.8 | 45 | 0 | 24-28 | 85 | 6.6 | Berawan |
| Jakarta Pusat | 13.7 | 54 | 0 | 24-32 | 84 | 9.4 | Cerah |
| Surabaya | 11.5 | 54 | 0 | 24-34 | 82 | 27.8 | Cerah Berawan |
| Denpasar | 11.5 | 24 | 0 | 25-33 | 85 | 29.5 | Berawan |
| Palembang | 11.2 | 30 | 0 | 24-31 | 88 | 6.1 | Berawan |
| Bandar Lampung | 8.6 | 42 | 0 | 24-30 | 85 | 10.9 | Berawan |
| Balikpapan | 7.6 | 54 | 0 | 24-29 | 86 | 13.4 | Berawan |
| Makassar | 7.6 | 33 | 0 | 26-31 | 84 | 17.4 | Berawan |
| Banda Aceh | 7.5 | 45 | 0 | 23-30 | 84 | 11.7 | Berawan |
| Kupang | 7.4 | 27 | 0 | 25-34 | 77 | 16.0 | Cerah |
| Ambon | 3.6 | 15 | 0 | 24-30 | 85 | 11.4 | Berawan |
| Jayapura | 3.6 | 42 | 0 | 24-30 | 87 | 10.8 | Cerah Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 130 | 32.7 | 17 |
| Cerah Berawan | 98 | 24.7 | 17 |
| Hujan Ringan | 87 | 21.9 | 18 |
| Cerah | 62 | 15.6 | 15 |
| Udara Kabur | 8 | 2.0 | 5 |
| Hujan Petir | 6 | 1.5 | 5 |
| Hujan Sedang | 3 | 0.8 | 2 |
| Petir | 3 | 0.8 | 2 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Bandung** 18 Nov 16:00: angin 40 km/jam (Hujan Petir)
- **Bandung** 19 Nov 16:00: angin 43 km/jam (Hujan Petir)
- **Bandung** 20 Nov 13:00: angin 46 km/jam (Hujan Ringan)
- **Bandung** 20 Nov 16:00: angin 46 km/jam (Hujan Ringan)
- **Bandung** 19 Nov 13:00: angin 30 km/jam (Hujan Sedang)
- **Bandung** 20 Nov 19:00: angin 35 km/jam (Hujan Ringan)
- **Bandung** 20 Nov 22:00: angin 35 km/jam (Cerah Berawan)
- **Kupang** 20 Nov 14:00: suhu 34 C (Cerah Berawan)
- **Kupang** 18 Nov 14:00: suhu 34 C (Hujan Petir)
- **Kupang** 19 Nov 14:00: suhu 34 C (Hujan Ringan)
- **Surabaya** 18 Nov 10:00: suhu 34 C (Cerah Berawan)

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
