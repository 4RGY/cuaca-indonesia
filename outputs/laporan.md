# Prakiraan Cuaca Indonesia

Analisis 19 kota, 411 slot prakiraan 3 jam (27 Okt 2026 sampai 29 Okt 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-10-27 00:33 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 30.7 mm dalam 66 jam.
- Paling kering: **Kupang** dengan 0.2 mm.
- Suhu tertinggi: **Semarang** 35 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 16.0 C (selisih harian rata-rata 6.9 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 30.7 | 42 | 0 | 19-27 | 89 | 7.2 | Berawan |
| Palembang | 18.6 | 51 | 0 | 24-31 | 87 | 12.8 | Udara Kabur |
| Medan | 17.1 | 39 | 0 | 24-31 | 89 | 9.4 | Berawan |
| Jakarta Pusat | 12.1 | 57 | 0 | 24-30 | 85 | 7.0 | Cerah Berawan |
| Bandar Lampung | 11.5 | 51 | 0 | 24-30 | 88 | 13.9 | Udara Kabur |
| Padang | 11.0 | 48 | 0 | 25-28 | 85 | 7.0 | Berawan |
| Semarang | 10.7 | 33 | 0 | 24-35 | 83 | 18.5 | Berawan |
| Pontianak | 10.6 | 42 | 0 | 24-32 | 92 | 11.8 | Berawan |
| Denpasar | 7.1 | 45 | 0 | 25-31 | 85 | 16.4 | Berawan |
| Surabaya | 6.7 | 36 | 0 | 24-33 | 80 | 12.7 | Cerah |
| Ambon | 6.0 | 21 | 0 | 23-31 | 85 | 13.1 | Udara Kabur |
| Jayapura | 5.6 | 39 | 0 | 23-29 | 87 | 12.1 | Cerah Berawan |
| Banda Aceh | 4.5 | 45 | 0 | 25-30 | 83 | 9.8 | Berawan |
| Balikpapan | 4.1 | 36 | 0 | 26-29 | 81 | 14.9 | Cerah |
| Manado | 2.9 | 21 | 0 | 24-31 | 79 | 12.8 | Cerah |
| Mataram | 2.5 | 30 | 0 | 23-32 | 80 | 23.3 | Cerah |
| Pekanbaru | 2.0 | 9 | 0 | 23-30 | 90 | 10.3 | Cerah Berawan |
| Makassar | 1.2 | 12 | 0 | 26-32 | 76 | 21.6 | Berawan |
| Kupang | 0.2 | 6 | 0 | 24-34 | 68 | 37.0 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah Berawan | 113 | 27.5 | 19 |
| Berawan | 112 | 27.3 | 17 |
| Cerah | 85 | 20.7 | 13 |
| Hujan Ringan | 49 | 11.9 | 15 |
| Udara Kabur | 47 | 11.4 | 9 |
| Hujan Petir | 3 | 0.7 | 2 |
| Hujan Sedang | 2 | 0.5 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 27 Oct 18:00: angin 37 km/jam (Cerah Berawan)
- **Kupang** 28 Oct 18:00: angin 37 km/jam (Cerah)
- **Semarang** 29 Oct 14:00: suhu 34 C (Cerah)
- **Semarang** 29 Oct 11:00: suhu 35 C (Cerah)
- **Kupang** 29 Oct 12:00: suhu 34 C (Berawan)
- **Kupang** 28 Oct 12:00: suhu 34 C (Cerah)

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
