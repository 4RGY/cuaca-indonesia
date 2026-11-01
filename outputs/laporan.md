# Prakiraan Cuaca Indonesia

Analisis 19 kota, 413 slot prakiraan 3 jam (1 Nov 2026 sampai 3 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-01 00:12 UTC.

## Angka kunci

- Paling basah: **Ambon** dengan 12.3 mm dalam 66 jam.
- Paling kering: **Surabaya** dengan 0.7 mm.
- Suhu tertinggi: **Surabaya** 37 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 18.0 C (selisih harian rata-rata 7.4 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Ambon | 12.3 | 33 | 0 | 23-32 | 88 | 13.0 | Hujan Ringan |
| Semarang | 11.7 | 36 | 0 | 25-34 | 73 | 15.1 | Cerah |
| Bandar Lampung | 10.5 | 48 | 0 | 24-31 | 84 | 12.6 | Cerah Berawan |
| Medan | 9.2 | 45 | 0 | 23-31 | 88 | 9.4 | Cerah |
| Manado | 9.2 | 33 | 0 | 24-30 | 84 | 8.8 | Cerah Berawan |
| Padang | 9.1 | 42 | 0 | 25-28 | 85 | 8.1 | Cerah |
| Pekanbaru | 8.2 | 54 | 0 | 23-30 | 89 | 9.9 | Cerah |
| Pontianak | 8.1 | 36 | 0 | 23-33 | 89 | 9.2 | Cerah |
| Bandung | 6.0 | 33 | 0 | 19-29 | 80 | 8.1 | Cerah |
| Palembang | 5.9 | 36 | 0 | 24-33 | 87 | 8.8 | Berawan |
| Jakarta Pusat | 4.8 | 42 | 0 | 25-31 | 79 | 9.4 | Cerah |
| Banda Aceh | 4.5 | 45 | 0 | 24-29 | 85 | 13.7 | Cerah Berawan |
| Mataram | 4.4 | 33 | 0 | 23-34 | 83 | 25.1 | Berawan |
| Balikpapan | 3.4 | 36 | 0 | 25-29 | 81 | 13.6 | Cerah |
| Denpasar | 3.4 | 6 | 0 | 24-32 | 86 | 18.6 | Cerah |
| Jayapura | 2.7 | 42 | 0 | 23-28 | 85 | 12.2 | Udara Kabur |
| Kupang | 1.4 | 15 | 0 | 25-34 | 71 | 37.1 | Cerah |
| Makassar | 1.3 | 33 | 0 | 26-30 | 78 | 21.1 | Cerah |
| Surabaya | 0.7 | 15 | 0 | 26-37 | 63 | 33.4 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 167 | 40.4 | 18 |
| Cerah Berawan | 87 | 21.1 | 18 |
| Berawan | 78 | 18.9 | 16 |
| Udara Kabur | 42 | 10.2 | 6 |
| Hujan Ringan | 36 | 8.7 | 13 |
| Hujan Petir | 1 | 0.2 | 1 |
| Kabut/Asap | 1 | 0.2 | 1 |
| Petir | 1 | 0.2 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 01 Nov 15:00: angin 37 km/jam (Cerah Berawan)
- **Surabaya** 03 Nov 13:00: angin 33 km/jam, suhu 37 C (Cerah)
- **Surabaya** 03 Nov 16:00: angin 33 km/jam (Cerah)
- **Surabaya** 01 Nov 13:00: angin 31 km/jam, suhu 37 C (Berawan)
- **Surabaya** 02 Nov 13:00: suhu 35 C (Cerah)
- **Kupang** 02 Nov 15:00: suhu 34 C (Cerah)
- **Mataram** 01 Nov 14:00: suhu 34 C (Berawan)
- **Mataram** 02 Nov 14:00: suhu 34 C (Berawan)
- **Kupang** 02 Nov 12:00: suhu 34 C (Cerah Berawan)
- **Semarang** 03 Nov 13:00: suhu 34 C (Cerah)
- **Semarang** 01 Nov 13:00: suhu 34 C (Berawan)
- **Surabaya** 01 Nov 16:00: suhu 34 C (Cerah Berawan)

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
