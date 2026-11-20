# Prakiraan Cuaca Indonesia

Analisis 19 kota, 397 slot prakiraan 3 jam (20 Nov 2026 sampai 22 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-20 02:24 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 29.3 mm dalam 63 jam.
- Paling kering: **Makassar** dengan 3.7 mm.
- Suhu tertinggi: **Surabaya** 37 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 17.0 C (selisih harian rata-rata 6.8 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 29.3 | 45 | 0 | 20-26 | 89 | 8.3 | Hujan Ringan |
| Medan | 21.0 | 45 | 0 | 24-31 | 91 | 7.4 | Hujan Ringan |
| Pontianak | 19.8 | 48 | 0 | 24-33 | 93 | 14.9 | Cerah Berawan |
| Semarang | 19.8 | 45 | 0 | 25-35 | 84 | 8.7 | Hujan Ringan |
| Manado | 18.1 | 24 | 0 | 24-32 | 88 | 8.6 | Cerah Berawan |
| Banda Aceh | 14.1 | 51 | 0 | 24-29 | 88 | 9.5 | Berawan |
| Denpasar | 14.0 | 51 | 0 | 25-31 | 85 | 25.4 | Cerah |
| Pekanbaru | 12.8 | 39 | 0 | 24-30 | 89 | 8.0 | Berawan |
| Palembang | 10.6 | 57 | 0 | 24-31 | 87 | 8.3 | Berawan |
| Jakarta Pusat | 9.6 | 45 | 0 | 24-30 | 83 | 7.2 | Cerah |
| Mataram | 9.2 | 42 | 0 | 24-33 | 87 | 23.7 | Cerah Berawan |
| Bandar Lampung | 8.6 | 51 | 0 | 24-30 | 88 | 10.6 | Berawan |
| Surabaya | 8.5 | 39 | 0 | 24-37 | 82 | 27.8 | Cerah |
| Balikpapan | 6.8 | 39 | 0 | 25-28 | 86 | 9.5 | Cerah Berawan |
| Kupang | 6.2 | 30 | 0 | 26-33 | 77 | 27.8 | Cerah |
| Jayapura | 5.4 | 27 | 0 | 23-30 | 90 | 17.0 | Cerah Berawan |
| Padang | 4.5 | 24 | 0 | 26-29 | 81 | 7.8 | Berawan |
| Ambon | 3.8 | 12 | 0 | 24-32 | 87 | 12.7 | Berawan |
| Makassar | 3.7 | 27 | 0 | 26-30 | 82 | 8.7 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah Berawan | 119 | 30.0 | 19 |
| Berawan | 99 | 24.9 | 18 |
| Cerah | 85 | 21.4 | 17 |
| Hujan Ringan | 72 | 18.1 | 18 |
| Udara Kabur | 14 | 3.5 | 5 |
| Hujan Petir | 6 | 1.5 | 4 |
| Kabut/Asap | 2 | 0.5 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Surabaya** 20 Nov 13:00: suhu 35 C (Hujan Petir)
- **Surabaya** 21 Nov 13:00: suhu 35 C (Cerah Berawan)
- **Surabaya** 22 Nov 13:00: suhu 37 C (Cerah)
- **Semarang** 21 Nov 12:00: suhu 34 C (Hujan Ringan)
- **Semarang** 22 Nov 12:00: suhu 35 C (Cerah)
- **Semarang** 20 Nov 15:00: suhu 34 C (Hujan Ringan)
- **Semarang** 20 Nov 12:00: suhu 34 C (Cerah Berawan)
- **Surabaya** 22 Nov 10:00: suhu 34 C (Cerah)

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
