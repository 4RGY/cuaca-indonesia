# Prakiraan Cuaca Indonesia

Analisis 19 kota, 402 slot prakiraan 3 jam (22 Nov 2026 sampai 24 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-11-22 01:25 UTC.

## Angka kunci

- Paling basah: **Semarang** dengan 20.9 mm dalam 63 jam.
- Paling kering: **Surabaya** dengan 2.2 mm.
- Suhu tertinggi: **Palembang** 34 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 14.0 C (selisih harian rata-rata 6.1 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Semarang | 20.9 | 45 | 0 | 26-32 | 82 | 10.1 | Cerah Berawan |
| Bandung | 20.2 | 39 | 0 | 20-27 | 87 | 7.0 | Berawan |
| Medan | 18.2 | 39 | 0 | 24-31 | 91 | 8.9 | Berawan |
| Pontianak | 13.4 | 48 | 0 | 24-31 | 90 | 9.2 | Berawan |
| Bandar Lampung | 11.8 | 48 | 0 | 24-29 | 89 | 9.2 | Cerah Berawan |
| Palembang | 11.6 | 42 | 0 | 24-34 | 89 | 6.5 | Berawan |
| Kupang | 9.9 | 33 | 0 | 26-32 | 77 | 13.9 | Cerah |
| Pekanbaru | 9.8 | 54 | 0 | 24-29 | 91 | 6.3 | Berawan |
| Banda Aceh | 9.3 | 39 | 0 | 24-28 | 89 | 12.0 | Berawan |
| Jakarta Pusat | 9.1 | 48 | 0 | 24-31 | 84 | 11.8 | Cerah Berawan |
| Padang | 8.5 | 36 | 0 | 25-28 | 86 | 5.3 | Berawan |
| Ambon | 7.7 | 6 | 0 | 24-33 | 87 | 9.6 | Cerah |
| Mataram | 5.8 | 51 | 0 | 25-32 | 85 | 18.0 | Cerah |
| Denpasar | 5.1 | 39 | 0 | 26-32 | 84 | 28.5 | Cerah |
| Jayapura | 4.1 | 48 | 0 | 24-29 | 87 | 20.7 | Cerah Berawan |
| Makassar | 4.1 | 24 | 0 | 26-30 | 82 | 11.8 | Berawan |
| Manado | 3.8 | 30 | 0 | 24-30 | 85 | 7.1 | Cerah |
| Balikpapan | 2.2 | 30 | 0 | 26-29 | 84 | 14.2 | Cerah |
| Surabaya | 2.2 | 21 | 0 | 24-33 | 80 | 11.5 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 121 | 30.1 | 19 |
| Cerah Berawan | 104 | 25.9 | 19 |
| Cerah | 97 | 24.1 | 16 |
| Hujan Ringan | 48 | 11.9 | 16 |
| Udara Kabur | 21 | 5.2 | 6 |
| Hujan Petir | 6 | 1.5 | 5 |
| Petir | 3 | 0.7 | 3 |
| Kabut/Asap | 1 | 0.2 | 1 |
| Hujan Sedang | 1 | 0.2 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Palembang** 22 Nov 15:00: suhu 34 C (Hujan Petir)
- **Palembang** 22 Nov 12:00: suhu 34 C (Cerah Berawan)
- **Palembang** 23 Nov 12:00: suhu 34 C (Berawan)

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
