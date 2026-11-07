# Prakiraan Cuaca Indonesia

Analisis 19 kota, 410 slot prakiraan 3 jam (7 Nov 2026 sampai 9 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-07 00:59 UTC.

## Angka kunci

- Paling basah: **Medan** dengan 22.2 mm dalam 66 jam.
- Paling kering: **Surabaya** dengan 0.2 mm.
- Suhu tertinggi: **Surabaya** 36 C.
- Suhu terendah: **Bandung** 18 C.
- Rentang suhu antar kota: 18.0 C (selisih harian rata-rata 6.7 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Medan | 22.2 | 45 | 0 | 23-30 | 90 | 10.2 | Berawan |
| Padang | 19.3 | 54 | 0 | 25-28 | 85 | 7.7 | Berawan |
| Pekanbaru | 17.0 | 36 | 0 | 23-30 | 90 | 6.7 | Cerah Berawan |
| Pontianak | 12.7 | 42 | 0 | 24-30 | 92 | 11.3 | Berawan |
| Ambon | 10.7 | 33 | 0 | 24-29 | 88 | 11.4 | Udara Kabur |
| Banda Aceh | 9.1 | 51 | 0 | 24-29 | 86 | 12.3 | Berawan |
| Balikpapan | 9.1 | 51 | 0 | 24-29 | 84 | 11.3 | Cerah Berawan |
| Manado | 8.2 | 45 | 0 | 24-29 | 85 | 8.2 | Cerah |
| Jakarta Pusat | 8.0 | 54 | 0 | 23-32 | 79 | 10.9 | Cerah Berawan |
| Palembang | 7.1 | 36 | 0 | 24-32 | 86 | 11.4 | Berawan |
| Mataram | 5.2 | 45 | 0 | 25-30 | 84 | 18.4 | Cerah |
| Bandar Lampung | 3.6 | 30 | 0 | 24-31 | 80 | 11.7 | Berawan |
| Bandung | 3.6 | 27 | 0 | 18-30 | 76 | 8.8 | Cerah |
| Kupang | 2.6 | 33 | 0 | 26-33 | 74 | 27.8 | Cerah |
| Semarang | 2.2 | 9 | 0 | 25-33 | 74 | 12.7 | Cerah |
| Denpasar | 1.9 | 36 | 0 | 25-33 | 79 | 27.8 | Cerah |
| Jayapura | 1.2 | 27 | 0 | 23-29 | 82 | 15.0 | Cerah Berawan |
| Makassar | 0.2 | 3 | 0 | 26-30 | 77 | 12.5 | Cerah |
| Surabaya | 0.2 | 3 | 0 | 25-36 | 65 | 13.8 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 143 | 34.9 | 19 |
| Cerah Berawan | 111 | 27.1 | 19 |
| Berawan | 87 | 21.2 | 15 |
| Hujan Ringan | 39 | 9.5 | 10 |
| Udara Kabur | 26 | 6.3 | 8 |
| Petir | 2 | 0.5 | 1 |
| Hujan Petir | 1 | 0.2 | 1 |
| Hujan Sedang | 1 | 0.2 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Surabaya** 08 Nov 14:00: suhu 35 C (Cerah)
- **Surabaya** 07 Nov 14:00: suhu 35 C (Cerah Berawan)
- **Surabaya** 07 Nov 11:00: suhu 35 C (Cerah)
- **Surabaya** 08 Nov 11:00: suhu 36 C (Cerah)
- **Surabaya** 09 Nov 11:00: suhu 34 C (Cerah)

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
