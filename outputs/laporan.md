# Prakiraan Cuaca Indonesia

Analisis 19 kota, 400 slot prakiraan 3 jam (6 Nov 2026 sampai 8 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-06 01:37 UTC.

## Angka kunci

- Paling basah: **Medan** dengan 21.6 mm dalam 63 jam.
- Paling kering: **Kupang** dengan 0.0 mm.
- Suhu tertinggi: **Surabaya** 38 C.
- Suhu terendah: **Bandung** 18 C.
- Rentang suhu antar kota: 20.0 C (selisih harian rata-rata 7.3 C).
- Kota tanpa hujan sama sekali: 3 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Medan | 21.6 | 54 | 0 | 23-30 | 89 | 9.7 | Berawan |
| Padang | 11.4 | 39 | 0 | 24-27 | 86 | 5.4 | Berawan |
| Pontianak | 9.9 | 33 | 0 | 23-31 | 91 | 8.6 | Berawan |
| Manado | 7.9 | 36 | 0 | 24-32 | 85 | 7.5 | Cerah Berawan |
| Ambon | 7.6 | 18 | 0 | 23-32 | 87 | 11.8 | Udara Kabur |
| Palembang | 7.4 | 36 | 0 | 24-32 | 85 | 10.4 | Berawan |
| Banda Aceh | 7.1 | 36 | 0 | 24-29 | 87 | 15.6 | Cerah |
| Bandar Lampung | 6.4 | 45 | 0 | 24-32 | 79 | 13.1 | Berawan |
| Balikpapan | 5.5 | 39 | 0 | 25-29 | 83 | 11.2 | Berawan |
| Mataram | 5.1 | 36 | 0 | 24-31 | 82 | 15.2 | Cerah |
| Semarang | 4.2 | 24 | 0 | 26-34 | 71 | 12.3 | Cerah |
| Jakarta Pusat | 4.1 | 39 | 0 | 25-32 | 75 | 10.5 | Cerah |
| Bandung | 3.3 | 18 | 0 | 18-30 | 71 | 9.1 | Cerah |
| Surabaya | 1.9 | 27 | 0 | 25-38 | 64 | 27.8 | Cerah |
| Makassar | 0.4 | 12 | 0 | 26-30 | 77 | 16.2 | Cerah |
| Pekanbaru | 0.2 | 3 | 0 | 24-30 | 88 | 6.2 | Cerah Berawan |
| Jayapura | 0.0 | 0 | 0 | 23-29 | 85 | 12.1 | Udara Kabur |
| Denpasar | 0.0 | 0 | 0 | 26-33 | 78 | 12.3 | Cerah |
| Kupang | 0.0 | 0 | 0 | 25-34 | 72 | 33.3 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 143 | 35.8 | 15 |
| Berawan | 83 | 20.8 | 16 |
| Cerah Berawan | 79 | 19.8 | 16 |
| Udara Kabur | 53 | 13.2 | 9 |
| Hujan Ringan | 37 | 9.2 | 11 |
| Hujan Petir | 3 | 0.8 | 2 |
| Petir | 2 | 0.5 | 2 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 06 Nov 16:00: angin 33 km/jam (Berawan)
- **Kupang** 07 Nov 16:00: angin 33 km/jam (Cerah Berawan)
- **Kupang** 08 Nov 13:00: angin 33 km/jam, suhu 34 C (Cerah)
- **Kupang** 08 Nov 16:00: angin 33 km/jam (Cerah Berawan)
- **Surabaya** 06 Nov 12:00: suhu 38 C (Cerah)
- **Surabaya** 07 Nov 12:00: suhu 37 C (Cerah Berawan)
- **Surabaya** 08 Nov 12:00: suhu 36 C (Cerah)
- **Surabaya** 08 Nov 15:00: suhu 35 C (Cerah)
- **Surabaya** 06 Nov 15:00: suhu 36 C (Cerah)
- **Surabaya** 07 Nov 15:00: suhu 35 C (Cerah)
- **Semarang** 07 Nov 12:00: suhu 34 C (Cerah)
- **Semarang** 08 Nov 12:00: suhu 34 C (Cerah)

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
