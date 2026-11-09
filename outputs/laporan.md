# Prakiraan Cuaca Indonesia

Analisis 19 kota, 410 slot prakiraan 3 jam (9 Nov 2026 sampai 11 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-09 00:59 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 19.8 mm dalam 66 jam.
- Paling kering: **Makassar** dengan 0.2 mm.
- Suhu tertinggi: **Semarang** 35 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 16.0 C (selisih harian rata-rata 7.1 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 19.8 | 18 | 0 | 19-30 | 82 | 6.6 | Cerah Berawan |
| Medan | 17.4 | 39 | 0 | 23-30 | 89 | 8.9 | Berawan |
| Semarang | 13.8 | 48 | 0 | 23-35 | 78 | 11.8 | Hujan Ringan |
| Padang | 12.6 | 54 | 0 | 25-27 | 84 | 6.0 | Berawan |
| Pontianak | 12.1 | 39 | 0 | 24-34 | 93 | 9.2 | Cerah Berawan |
| Banda Aceh | 10.6 | 54 | 0 | 24-29 | 88 | 10.7 | Berawan |
| Ambon | 10.2 | 30 | 0 | 24-29 | 87 | 11.6 | Cerah |
| Palembang | 7.4 | 39 | 0 | 24-33 | 84 | 10.4 | Berawan |
| Manado | 7.4 | 30 | 0 | 23-31 | 86 | 9.7 | Cerah Berawan |
| Pekanbaru | 6.8 | 30 | 0 | 24-30 | 89 | 7.7 | Berawan |
| Mataram | 6.1 | 51 | 0 | 24-30 | 85 | 10.8 | Cerah |
| Bandar Lampung | 4.0 | 36 | 0 | 24-31 | 77 | 13.9 | Cerah |
| Denpasar | 4.0 | 48 | 0 | 24-30 | 82 | 10.8 | Cerah |
| Jakarta Pusat | 4.0 | 54 | 0 | 25-33 | 75 | 8.7 | Berawan |
| Balikpapan | 3.8 | 24 | 0 | 25-29 | 84 | 11.1 | Berawan |
| Kupang | 3.5 | 27 | 0 | 25-34 | 75 | 9.9 | Cerah |
| Surabaya | 3.0 | 48 | 0 | 24-35 | 71 | 11.5 | Cerah |
| Jayapura | 1.6 | 33 | 0 | 23-29 | 84 | 10.5 | Cerah Berawan |
| Makassar | 0.2 | 6 | 0 | 27-30 | 74 | 14.3 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 119 | 29.0 | 16 |
| Berawan | 118 | 28.8 | 17 |
| Cerah Berawan | 112 | 27.3 | 19 |
| Hujan Ringan | 45 | 11.0 | 13 |
| Udara Kabur | 14 | 3.4 | 6 |
| Hujan Sedang | 1 | 0.2 | 1 |
| Petir | 1 | 0.2 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Semarang** 09 Nov 14:00: suhu 35 C (Hujan Ringan)
- **Surabaya** 09 Nov 14:00: suhu 35 C (Cerah)
- **Kupang** 09 Nov 12:00: suhu 34 C (Cerah)
- **Pontianak** 11 Nov 11:00: suhu 34 C (Cerah Berawan)
- **Semarang** 11 Nov 11:00: suhu 34 C (Berawan)
- **Surabaya** 10 Nov 11:00: suhu 34 C (Berawan)
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
