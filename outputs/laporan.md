# Prakiraan Cuaca Indonesia

Analisis 19 kota, 397 slot prakiraan 3 jam (12 Nov 2026 sampai 14 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-12 02:18 UTC.

## Angka kunci

- Paling basah: **Medan** dengan 25.6 mm dalam 63 jam.
- Paling kering: **Denpasar** dengan 0.0 mm.
- Suhu tertinggi: **Bandar Lampung** 35 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 15.0 C (selisih harian rata-rata 7.0 C).
- Kota tanpa hujan sama sekali: 2 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Medan | 25.6 | 51 | 0 | 24-31 | 90 | 8.7 | Berawan |
| Bandar Lampung | 21.2 | 51 | 0 | 24-35 | 79 | 15.6 | Hujan Ringan |
| Pontianak | 19.7 | 45 | 0 | 24-32 | 92 | 10.4 | Berawan |
| Pekanbaru | 14.7 | 63 | 0 | 24-31 | 88 | 8.9 | Berawan |
| Semarang | 13.0 | 36 | 0 | 26-33 | 80 | 13.9 | Cerah |
| Bandung | 11.8 | 27 | 0 | 20-28 | 82 | 7.7 | Berawan |
| Palembang | 9.9 | 45 | 0 | 24-31 | 88 | 6.7 | Berawan |
| Padang | 9.9 | 51 | 0 | 25-28 | 86 | 5.6 | Berawan |
| Banda Aceh | 7.3 | 33 | 0 | 24-30 | 87 | 13.1 | Berawan |
| Manado | 6.4 | 30 | 0 | 24-30 | 85 | 7.8 | Cerah |
| Jakarta Pusat | 5.8 | 36 | 0 | 26-32 | 79 | 10.8 | Berawan |
| Balikpapan | 5.0 | 42 | 0 | 25-29 | 84 | 14.6 | Berawan |
| Mataram | 4.6 | 30 | 0 | 24-32 | 81 | 12.5 | Cerah |
| Ambon | 3.4 | 6 | 0 | 24-30 | 86 | 12.4 | Cerah Berawan |
| Surabaya | 2.6 | 30 | 0 | 25-35 | 72 | 14.4 | Cerah |
| Makassar | 2.5 | 9 | 0 | 27-35 | 80 | 9.7 | Cerah |
| Jayapura | 1.8 | 36 | 0 | 24-28 | 86 | 16.9 | Cerah Berawan |
| Kupang | 0.0 | 0 | 0 | 25-35 | 65 | 37.0 | Cerah |
| Denpasar | 0.0 | 0 | 0 | 25-32 | 82 | 21.3 | Cerah Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 107 | 27.0 | 18 |
| Berawan | 106 | 26.7 | 17 |
| Cerah Berawan | 104 | 26.2 | 18 |
| Hujan Ringan | 61 | 15.4 | 13 |
| Udara Kabur | 16 | 4.0 | 7 |
| Petir | 2 | 0.5 | 1 |
| Hujan Sedang | 1 | 0.3 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 13 Nov 17:00: angin 37 km/jam (Cerah Berawan)
- **Kupang** 13 Nov 14:00: suhu 34 C (Cerah Berawan)
- **Kupang** 14 Nov 14:00: suhu 34 C (Cerah Berawan)
- **Kupang** 12 Nov 14:00: suhu 34 C (Cerah Berawan)
- **Kupang** 13 Nov 11:00: suhu 34 C (Cerah)
- **Surabaya** 12 Nov 13:00: suhu 34 C (Cerah)
- **Bandar Lampung** 12 Nov 13:00: suhu 35 C (Hujan Ringan)
- **Surabaya** 13 Nov 13:00: suhu 35 C (Cerah)
- **Makassar** 13 Nov 14:00: suhu 35 C (Cerah)
- **Makassar** 14 Nov 14:00: suhu 35 C (Cerah)
- **Surabaya** 14 Nov 13:00: suhu 35 C (Berawan)
- **Kupang** 14 Nov 11:00: suhu 35 C (Cerah Berawan)

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
