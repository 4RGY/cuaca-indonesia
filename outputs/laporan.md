# Prakiraan Cuaca Indonesia

Analisis 19 kota, 393 slot prakiraan 3 jam (26 Nov 2026 sampai 28 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-26 03:38 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 50.5 mm dalam 63 jam.
- Paling kering: **Balikpapan** dengan 2.2 mm.
- Suhu tertinggi: **Kupang** 34 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 15.0 C (selisih harian rata-rata 6.4 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 50.5 | 39 | 0 | 19-25 | 91 | 50.1 | Berawan |
| Padang | 43.0 | 60 | 0 | 25-28 | 87 | 9.3 | Hujan Ringan |
| Medan | 20.6 | 57 | 0 | 23-30 | 92 | 9.0 | Berawan |
| Palembang | 16.5 | 54 | 0 | 24-30 | 89 | 5.9 | Berawan |
| Bandar Lampung | 15.1 | 57 | 0 | 24-30 | 88 | 13.7 | Berawan |
| Jakarta Pusat | 14.7 | 51 | 0 | 24-30 | 86 | 7.6 | Berawan |
| Pekanbaru | 13.4 | 15 | 0 | 24-30 | 91 | 11.4 | Berawan |
| Kupang | 13.4 | 39 | 0 | 25-34 | 83 | 27.8 | Cerah |
| Pontianak | 12.7 | 48 | 0 | 24-32 | 91 | 11.8 | Berawan |
| Semarang | 12.1 | 36 | 0 | 25-32 | 84 | 10.8 | Berawan |
| Mataram | 11.3 | 45 | 0 | 23-32 | 87 | 27.8 | Berawan |
| Surabaya | 7.7 | 51 | 0 | 25-34 | 84 | 28.6 | Berawan |
| Ambon | 6.6 | 30 | 0 | 25-31 | 86 | 10.5 | Berawan |
| Manado | 4.9 | 42 | 0 | 25-32 | 85 | 18.5 | Cerah |
| Banda Aceh | 4.9 | 45 | 0 | 25-29 | 86 | 11.8 | Berawan |
| Jayapura | 4.5 | 45 | 0 | 24-28 | 89 | 16.3 | Cerah Berawan |
| Makassar | 3.9 | 9 | 0 | 26-33 | 82 | 9.3 | Berawan |
| Denpasar | 2.5 | 6 | 0 | 25-32 | 83 | 27.8 | Berawan |
| Balikpapan | 2.2 | 30 | 0 | 24-29 | 86 | 14.6 | Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 191 | 48.6 | 19 |
| Cerah Berawan | 72 | 18.3 | 16 |
| Hujan Ringan | 57 | 14.5 | 15 |
| Cerah | 49 | 12.5 | 10 |
| Udara Kabur | 12 | 3.1 | 5 |
| Hujan Petir | 7 | 1.8 | 4 |
| Hujan Sedang | 3 | 0.8 | 3 |
| Petir | 2 | 0.5 | 2 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Bandung** 26 Nov 14:00: angin 43 km/jam (Hujan Petir)
- **Bandung** 27 Nov 14:00: angin 50 km/jam (Hujan Sedang)
- **Bandung** 28 Nov 14:00: angin 36 km/jam (Hujan Ringan)
- **Bandung** 28 Nov 11:00: angin 36 km/jam (Hujan Ringan)
- **Surabaya** 26 Nov 11:00: suhu 34 C (Berawan)
- **Surabaya** 27 Nov 11:00: suhu 34 C (Berawan)
- **Kupang** 26 Nov 12:00: suhu 34 C (Hujan Petir)
- **Surabaya** 28 Nov 11:00: suhu 34 C (Berawan)
- **Kupang** 28 Nov 12:00: suhu 34 C (Berawan)

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
