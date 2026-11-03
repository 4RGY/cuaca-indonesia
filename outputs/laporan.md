# Prakiraan Cuaca Indonesia

Analisis 19 kota, 397 slot prakiraan 3 jam (3 Nov 2026 sampai 5 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-03 02:57 UTC.

## Angka kunci

- Paling basah: **Pontianak** dengan 14.5 mm dalam 63 jam.
- Paling kering: **Surabaya** dengan 0.3 mm.
- Suhu tertinggi: **Surabaya** 36 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 17.0 C (selisih harian rata-rata 6.8 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Pontianak | 14.5 | 45 | 0 | 23-31 | 90 | 9.2 | Hujan Ringan |
| Padang | 11.7 | 57 | 0 | 25-27 | 86 | 9.4 | Berawan |
| Medan | 10.1 | 42 | 0 | 23-31 | 89 | 6.3 | Berawan |
| Palembang | 8.6 | 51 | 0 | 23-31 | 88 | 12.6 | Berawan |
| Pekanbaru | 7.8 | 54 | 0 | 24-31 | 89 | 8.6 | Berawan |
| Bandar Lampung | 6.0 | 45 | 0 | 24-32 | 84 | 11.6 | Berawan |
| Ambon | 4.9 | 30 | 0 | 24-29 | 85 | 13.6 | Cerah Berawan |
| Jayapura | 4.5 | 39 | 0 | 23-28 | 84 | 10.5 | Cerah |
| Jakarta Pusat | 4.4 | 33 | 0 | 25-32 | 73 | 12.9 | Cerah |
| Banda Aceh | 3.8 | 30 | 0 | 24-30 | 84 | 16.7 | Berawan |
| Mataram | 3.4 | 33 | 0 | 25-32 | 78 | 15.0 | Cerah |
| Manado | 2.9 | 24 | 0 | 23-30 | 82 | 8.0 | Cerah |
| Bandung | 2.8 | 33 | 0 | 19-30 | 74 | 9.1 | Cerah |
| Balikpapan | 2.5 | 36 | 0 | 25-30 | 80 | 13.3 | Cerah |
| Semarang | 2.2 | 24 | 0 | 26-35 | 69 | 14.5 | Cerah |
| Denpasar | 0.7 | 15 | 0 | 25-30 | 81 | 17.2 | Cerah |
| Makassar | 0.6 | 15 | 0 | 27-31 | 77 | 18.0 | Cerah |
| Kupang | 0.5 | 9 | 0 | 24-32 | 71 | 11.8 | Cerah |
| Surabaya | 0.3 | 9 | 0 | 26-36 | 61 | 17.7 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 148 | 37.3 | 16 |
| Berawan | 101 | 25.4 | 15 |
| Cerah Berawan | 84 | 21.2 | 18 |
| Udara Kabur | 34 | 8.6 | 13 |
| Hujan Ringan | 27 | 6.8 | 10 |
| Petir | 2 | 0.5 | 1 |
| Kabut/Asap | 1 | 0.3 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Surabaya** 03 Nov 13:00: suhu 35 C (Cerah)
- **Semarang** 03 Nov 13:00: suhu 35 C (Cerah)
- **Surabaya** 04 Nov 13:00: suhu 35 C (Cerah)
- **Surabaya** 03 Nov 10:00: suhu 34 C (Cerah)
- **Surabaya** 05 Nov 13:00: suhu 36 C (Cerah)
- **Surabaya** 05 Nov 16:00: suhu 34 C (Cerah)
- **Semarang** 04 Nov 13:00: suhu 34 C (Cerah)
- **Semarang** 04 Nov 10:00: suhu 34 C (Cerah)
- **Surabaya** 04 Nov 10:00: suhu 35 C (Cerah)
- **Surabaya** 05 Nov 10:00: suhu 35 C (Cerah)

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
