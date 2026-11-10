# Prakiraan Cuaca Indonesia

Analisis 19 kota, 395 slot prakiraan 3 jam (10 Nov 2026 sampai 12 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-10 03:39 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 18.9 mm dalam 63 jam.
- Paling kering: **Makassar** dengan 1.2 mm.
- Suhu tertinggi: **Kupang** 35 C.
- Suhu terendah: **Bandung** 18 C.
- Rentang suhu antar kota: 17.0 C (selisih harian rata-rata 7.6 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 18.9 | 36 | 0 | 18-28 | 82 | 6.4 | Cerah Berawan |
| Semarang | 16.3 | 45 | 0 | 25-32 | 79 | 12.0 | Cerah Berawan |
| Pekanbaru | 16.0 | 33 | 0 | 24-30 | 89 | 7.3 | Berawan |
| Medan | 15.6 | 39 | 0 | 24-31 | 89 | 7.9 | Berawan |
| Banda Aceh | 13.7 | 63 | 0 | 24-28 | 89 | 14.8 | Berawan |
| Pontianak | 13.5 | 48 | 0 | 24-33 | 92 | 10.9 | Cerah Berawan |
| Mataram | 11.8 | 24 | 0 | 24-34 | 78 | 22.2 | Cerah |
| Manado | 10.2 | 30 | 0 | 23-32 | 86 | 8.3 | Cerah |
| Ambon | 8.0 | 27 | 0 | 24-32 | 87 | 11.9 | Cerah |
| Padang | 6.8 | 48 | 0 | 25-28 | 84 | 8.6 | Berawan |
| Kupang | 6.7 | 15 | 0 | 25-35 | 78 | 37.1 | Cerah |
| Palembang | 6.2 | 33 | 0 | 24-34 | 82 | 8.9 | Berawan |
| Denpasar | 5.6 | 15 | 0 | 23-32 | 81 | 27.8 | Cerah Berawan |
| Balikpapan | 5.5 | 36 | 0 | 25-29 | 83 | 12.7 | Berawan |
| Jakarta Pusat | 4.9 | 48 | 0 | 26-32 | 75 | 10.6 | Berawan |
| Surabaya | 4.0 | 42 | 0 | 25-35 | 73 | 31.2 | Berawan |
| Bandar Lampung | 3.2 | 33 | 0 | 24-32 | 76 | 14.6 | Berawan |
| Jayapura | 3.2 | 39 | 0 | 24-31 | 84 | 13.2 | Cerah Berawan |
| Makassar | 1.2 | 6 | 0 | 26-34 | 77 | 13.9 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah Berawan | 130 | 32.9 | 18 |
| Berawan | 120 | 30.4 | 15 |
| Cerah | 79 | 20.0 | 16 |
| Hujan Ringan | 54 | 13.7 | 15 |
| Udara Kabur | 10 | 2.5 | 5 |
| Hujan Petir | 2 | 0.5 | 2 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 12 Nov 12:00: angin 37 km/jam, suhu 35 C (Cerah)
- **Kupang** 12 Nov 15:00: angin 37 km/jam, suhu 34 C (Cerah)
- **Surabaya** 10 Nov 13:00: angin 31 km/jam, suhu 34 C (Udara Kabur)
- **Mataram** 10 Nov 11:00: suhu 34 C (Cerah Berawan)
- **Kupang** 11 Nov 12:00: suhu 34 C (Cerah Berawan)
- **Surabaya** 12 Nov 13:00: suhu 34 C (Cerah Berawan)
- **Kupang** 10 Nov 12:00: suhu 34 C (Hujan Ringan)
- **Makassar** 12 Nov 12:00: suhu 34 C (Cerah)
- **Makassar** 12 Nov 15:00: suhu 34 C (Cerah)
- **Palembang** 11 Nov 16:00: suhu 34 C (Hujan Ringan)
- **Surabaya** 10 Nov 10:00: suhu 35 C (Cerah Berawan)

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
