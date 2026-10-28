# Prakiraan Cuaca Indonesia

Analisis 19 kota, 410 slot prakiraan 3 jam (28 Okt 2026 sampai 30 Okt 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-10-28 00:34 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 31.9 mm dalam 66 jam.
- Paling kering: **Manado** dengan 0.7 mm.
- Suhu tertinggi: **Surabaya** 36 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 17.0 C (selisih harian rata-rata 6.9 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 31.9 | 33 | 0 | 19-31 | 88 | 5.9 | Hujan Ringan |
| Medan | 14.8 | 39 | 0 | 23-31 | 87 | 10.8 | Berawan |
| Palembang | 14.6 | 42 | 0 | 24-30 | 88 | 6.7 | Berawan |
| Bandar Lampung | 13.4 | 54 | 0 | 24-30 | 88 | 12.2 | Berawan |
| Semarang | 13.1 | 33 | 0 | 25-33 | 83 | 17.8 | Cerah |
| Jakarta Pusat | 9.3 | 48 | 0 | 24-30 | 85 | 7.4 | Berawan |
| Padang | 8.7 | 57 | 0 | 25-28 | 86 | 6.3 | Berawan |
| Pontianak | 8.1 | 48 | 0 | 24-30 | 91 | 10.0 | Udara Kabur |
| Pekanbaru | 5.6 | 30 | 0 | 23-30 | 90 | 8.3 | Berawan |
| Mataram | 4.9 | 27 | 0 | 24-32 | 81 | 27.8 | Cerah |
| Banda Aceh | 4.7 | 42 | 0 | 25-29 | 85 | 13.6 | Berawan |
| Denpasar | 4.7 | 51 | 0 | 25-30 | 86 | 18.3 | Cerah Berawan |
| Balikpapan | 4.3 | 33 | 0 | 25-29 | 80 | 15.0 | Berawan |
| Surabaya | 2.3 | 36 | 0 | 24-36 | 74 | 18.5 | Cerah |
| Ambon | 2.1 | 21 | 0 | 25-32 | 83 | 14.2 | Udara Kabur |
| Makassar | 1.8 | 6 | 0 | 27-33 | 69 | 21.6 | Cerah Berawan |
| Kupang | 1.2 | 12 | 0 | 25-34 | 68 | 21.9 | Cerah |
| Jayapura | 1.1 | 18 | 0 | 23-29 | 83 | 15.0 | Udara Kabur |
| Manado | 0.7 | 15 | 0 | 24-32 | 72 | 10.6 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 115 | 28.0 | 16 |
| Cerah | 110 | 26.8 | 13 |
| Udara Kabur | 82 | 20.0 | 10 |
| Cerah Berawan | 61 | 14.9 | 15 |
| Hujan Ringan | 39 | 9.5 | 12 |
| Hujan Sedang | 2 | 0.5 | 1 |
| Petir | 1 | 0.2 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Surabaya** 29 Oct 14:00: suhu 36 C (Cerah)
- **Surabaya** 30 Oct 14:00: suhu 34 C (Cerah Berawan)
- **Surabaya** 30 Oct 11:00: suhu 34 C (Cerah)
- **Kupang** 30 Oct 12:00: suhu 34 C (Cerah)
- **Kupang** 28 Oct 12:00: suhu 34 C (Cerah Berawan)
- **Surabaya** 29 Oct 11:00: suhu 35 C (Cerah Berawan)

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
