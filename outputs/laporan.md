# Prakiraan Cuaca Indonesia

Analisis 19 kota, 392 slot prakiraan 3 jam (28 Nov 2026 sampai 30 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-28 03:21 UTC.

## Angka kunci

- Paling basah: **Pekanbaru** dengan 62.3 mm dalam 63 jam.
- Paling kering: **Jayapura** dengan 2.9 mm.
- Suhu tertinggi: **Pontianak** 33 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 13.0 C (selisih harian rata-rata 6.6 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Pekanbaru | 62.3 | 48 | 0 | 24-30 | 92 | 10.3 | Hujan Ringan |
| Bandung | 29.0 | 36 | 0 | 20-30 | 90 | 6.8 | Berawan |
| Medan | 23.9 | 57 | 0 | 23-30 | 90 | 6.0 | Hujan Ringan |
| Palembang | 23.4 | 48 | 0 | 24-31 | 91 | 12.1 | Berawan |
| Pontianak | 22.0 | 48 | 0 | 24-33 | 93 | 11.7 | Berawan |
| Surabaya | 19.9 | 57 | 0 | 25-32 | 84 | 13.9 | Hujan Ringan |
| Semarang | 19.7 | 33 | 0 | 25-31 | 86 | 10.7 | Berawan |
| Bandar Lampung | 18.5 | 51 | 0 | 24-32 | 89 | 13.2 | Berawan |
| Padang | 17.5 | 51 | 0 | 25-28 | 85 | 10.2 | Berawan |
| Mataram | 16.8 | 42 | 0 | 24-31 | 88 | 27.8 | Hujan Ringan |
| Jakarta Pusat | 14.1 | 39 | 0 | 24-31 | 86 | 8.0 | Berawan |
| Banda Aceh | 7.8 | 39 | 0 | 24-29 | 88 | 14.6 | Berawan |
| Denpasar | 7.5 | 45 | 0 | 25-31 | 85 | 15.7 | Cerah |
| Ambon | 7.0 | 21 | 0 | 25-32 | 81 | 10.2 | Berawan |
| Balikpapan | 5.7 | 30 | 0 | 25-30 | 84 | 13.9 | Berawan |
| Makassar | 5.4 | 18 | 0 | 26-33 | 84 | 10.9 | Berawan |
| Kupang | 3.6 | 30 | 0 | 25-33 | 79 | 12.6 | Cerah Berawan |
| Manado | 3.2 | 27 | 0 | 25-30 | 80 | 8.2 | Cerah |
| Jayapura | 2.9 | 36 | 0 | 23-29 | 85 | 16.4 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 138 | 35.2 | 19 |
| Hujan Ringan | 79 | 20.2 | 16 |
| Cerah | 73 | 18.6 | 15 |
| Cerah Berawan | 65 | 16.6 | 18 |
| Udara Kabur | 22 | 5.6 | 5 |
| Hujan Sedang | 8 | 2.0 | 3 |
| Hujan Petir | 5 | 1.3 | 3 |
| Hujan Lebat | 1 | 0.3 | 1 |
| Kabut/Asap | 1 | 0.3 | 1 |

## Peringatan dini

Tidak ada slot yang melewati ambang pada horizon prakiraan ini.

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
