# Prakiraan Cuaca Indonesia

Analisis 19 kota, 406 slot prakiraan 3 jam (4 Nov 2026 sampai 6 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-04 01:28 UTC.

## Angka kunci

- Paling basah: **Medan** dengan 17.4 mm dalam 63 jam.
- Paling kering: **Kupang** dengan 0.0 mm.
- Suhu tertinggi: **Surabaya** 36 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 16.0 C (selisih harian rata-rata 7.2 C).
- Kota tanpa hujan sama sekali: 1 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Medan | 17.4 | 57 | 0 | 23-31 | 88 | 7.9 | Cerah Berawan |
| Bandar Lampung | 16.7 | 48 | 0 | 23-31 | 85 | 10.3 | Cerah |
| Pekanbaru | 11.4 | 57 | 0 | 23-30 | 89 | 7.1 | Berawan |
| Banda Aceh | 11.0 | 54 | 0 | 24-28 | 87 | 11.5 | Berawan |
| Pontianak | 11.0 | 36 | 0 | 23-32 | 92 | 11.6 | Cerah Berawan |
| Palembang | 9.6 | 36 | 0 | 24-31 | 87 | 8.3 | Berawan |
| Padang | 8.9 | 42 | 0 | 25-27 | 86 | 7.5 | Berawan |
| Balikpapan | 6.2 | 39 | 0 | 25-30 | 82 | 14.7 | Berawan |
| Jakarta Pusat | 5.0 | 42 | 0 | 26-33 | 73 | 15.5 | Berawan |
| Ambon | 4.9 | 27 | 0 | 24-30 | 85 | 13.9 | Cerah |
| Manado | 4.0 | 30 | 0 | 24-32 | 81 | 8.3 | Cerah |
| Semarang | 4.0 | 30 | 0 | 25-34 | 73 | 12.5 | Berawan |
| Jayapura | 2.8 | 24 | 0 | 23-29 | 84 | 11.5 | Cerah |
| Mataram | 2.8 | 33 | 0 | 24-32 | 80 | 16.8 | Cerah |
| Denpasar | 2.6 | 21 | 0 | 24-31 | 82 | 15.3 | Cerah Berawan |
| Surabaya | 1.8 | 21 | 0 | 25-36 | 64 | 17.9 | Cerah |
| Bandung | 1.7 | 9 | 0 | 20-32 | 72 | 10.3 | Berawan |
| Makassar | 0.2 | 6 | 0 | 27-30 | 77 | 14.9 | Cerah |
| Kupang | 0.0 | 0 | 0 | 25-34 | 70 | 27.8 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 147 | 36.2 | 17 |
| Berawan | 108 | 26.6 | 15 |
| Cerah Berawan | 101 | 24.9 | 19 |
| Hujan Ringan | 29 | 7.1 | 10 |
| Udara Kabur | 16 | 3.9 | 7 |
| Kabut/Asap | 2 | 0.5 | 1 |
| Petir | 2 | 0.5 | 1 |
| Hujan Petir | 1 | 0.2 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 04 Nov 13:00: suhu 34 C (Cerah Berawan)
- **Kupang** 05 Nov 13:00: suhu 34 C (Cerah)
- **Kupang** 06 Nov 13:00: suhu 34 C (Cerah)
- **Surabaya** 04 Nov 14:00: suhu 34 C (Cerah)
- **Surabaya** 05 Nov 14:00: suhu 36 C (Cerah)
- **Surabaya** 06 Nov 11:00: suhu 35 C (Cerah)
- **Surabaya** 06 Nov 14:00: suhu 35 C (Cerah)
- **Semarang** 05 Nov 11:00: suhu 34 C (Cerah)
- **Semarang** 05 Nov 14:00: suhu 34 C (Cerah Berawan)
- **Semarang** 04 Nov 11:00: suhu 34 C (Cerah)
- **Surabaya** 04 Nov 11:00: suhu 35 C (Cerah)
- **Surabaya** 05 Nov 11:00: suhu 36 C (Cerah)

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
