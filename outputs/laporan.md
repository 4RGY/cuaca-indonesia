# Prakiraan Cuaca Indonesia

Analisis 19 kota, 403 slot prakiraan 3 jam (14 Nov 2026 sampai 16 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-14 01:29 UTC.

## Angka kunci

- Paling basah: **Padang** dengan 25.2 mm dalam 63 jam.
- Paling kering: **Surabaya** dengan 1.4 mm.
- Suhu tertinggi: **Surabaya** 37 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 18.0 C (selisih harian rata-rata 6.8 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Padang | 25.2 | 63 | 0 | 25-28 | 86 | 6.0 | Hujan Ringan |
| Medan | 23.8 | 51 | 0 | 23-30 | 91 | 8.3 | Berawan |
| Ambon | 20.2 | 36 | 0 | 24-31 | 89 | 9.0 | Hujan Ringan |
| Pekanbaru | 19.5 | 60 | 0 | 24-30 | 91 | 10.1 | Hujan Ringan |
| Banda Aceh | 17.8 | 60 | 0 | 24-29 | 89 | 9.9 | Berawan |
| Mataram | 13.8 | 33 | 0 | 25-32 | 82 | 18.5 | Cerah |
| Bandung | 13.6 | 36 | 0 | 19-28 | 87 | 7.9 | Berawan |
| Pontianak | 13.4 | 54 | 0 | 24-34 | 91 | 9.5 | Berawan |
| Manado | 11.5 | 24 | 0 | 25-31 | 83 | 7.9 | Cerah Berawan |
| Semarang | 10.5 | 33 | 0 | 26-34 | 79 | 12.1 | Berawan |
| Bandar Lampung | 10.4 | 39 | 0 | 24-32 | 86 | 11.7 | Cerah Berawan |
| Palembang | 9.0 | 51 | 0 | 24-32 | 89 | 8.8 | Berawan |
| Balikpapan | 8.1 | 42 | 0 | 25-30 | 84 | 14.7 | Berawan |
| Jakarta Pusat | 5.8 | 42 | 0 | 26-32 | 77 | 7.8 | Berawan |
| Jayapura | 4.2 | 45 | 0 | 24-29 | 88 | 8.0 | Berawan |
| Makassar | 4.0 | 36 | 0 | 26-31 | 80 | 14.9 | Cerah |
| Denpasar | 3.0 | 33 | 0 | 26-31 | 82 | 15.0 | Cerah |
| Kupang | 1.5 | 15 | 0 | 27-36 | 71 | 18.2 | Cerah |
| Surabaya | 1.4 | 18 | 0 | 26-37 | 68 | 16.3 | Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 154 | 38.2 | 18 |
| Cerah Berawan | 74 | 18.4 | 15 |
| Cerah | 71 | 17.6 | 11 |
| Hujan Ringan | 68 | 16.9 | 14 |
| Udara Kabur | 28 | 6.9 | 9 |
| Hujan Petir | 3 | 0.7 | 2 |
| Hujan Sedang | 3 | 0.7 | 3 |
| Petir | 2 | 0.5 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

Ditampilkan 12 slot teratas dari 14 slot.

- **Surabaya** 14 Nov 12:00: suhu 36 C (Cerah)
- **Surabaya** 15 Nov 12:00: suhu 37 C (Berawan)
- **Surabaya** 15 Nov 15:00: suhu 36 C (Berawan)
- **Semarang** 16 Nov 12:00: suhu 34 C (Berawan)
- **Semarang** 14 Nov 12:00: suhu 34 C (Berawan)
- **Kupang** 14 Nov 10:00: suhu 34 C (Berawan)
- **Surabaya** 14 Nov 15:00: suhu 35 C (Cerah)
- **Kupang** 16 Nov 13:00: suhu 36 C (Cerah Berawan)
- **Semarang** 15 Nov 12:00: suhu 34 C (Berawan)
- **Kupang** 14 Nov 13:00: suhu 36 C (Berawan)
- **Pontianak** 14 Nov 12:00: suhu 34 C (Cerah Berawan)
- **Kupang** 15 Nov 13:00: suhu 35 C (Cerah Berawan)

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
