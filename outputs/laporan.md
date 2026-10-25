# Prakiraan Cuaca Indonesia

Analisis 19 kota, 333 slot prakiraan 3 jam (26 Okt 2026 sampai 28 Okt 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-10-25 23:20 UTC.

## Angka kunci

- Paling basah: **Medan** dengan 9.2 mm dalam 51 jam.
- Paling kering: **Makassar** dengan 0.0 mm.
- Suhu tertinggi: **Surabaya** 36 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 17.0 C (selisih harian rata-rata 7.1 C).
- Kota tanpa hujan sama sekali: 1 dari 19.

## Ringkasan per kota

| Kota | Hujan 51 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Medan | 9.2 | 36 | 0 | 23-30 | 92 | 7.5 | Cerah Berawan |
| Bandung | 8.2 | 18 | 0 | 19-26 | 88 | 7.2 | Berawan |
| Pontianak | 7.1 | 24 | 0 | 24-30 | 93 | 10.0 | Udara Kabur |
| Jakarta Pusat | 6.6 | 33 | 0 | 24-30 | 83 | 11.6 | Berawan |
| Balikpapan | 5.9 | 36 | 0 | 24-30 | 84 | 12.8 | Udara Kabur |
| Pekanbaru | 5.3 | 12 | 0 | 23-31 | 89 | 6.5 | Cerah Berawan |
| Banda Aceh | 4.7 | 27 | 0 | 24-28 | 88 | 10.2 | Berawan |
| Semarang | 4.7 | 24 | 0 | 25-34 | 83 | 11.7 | Cerah |
| Palembang | 4.7 | 18 | 0 | 24-31 | 85 | 10.8 | Udara Kabur |
| Bandar Lampung | 3.7 | 18 | 0 | 24-30 | 80 | 17.8 | Berawan |
| Ambon | 2.7 | 24 | 0 | 23-30 | 88 | 11.6 | Udara Kabur |
| Denpasar | 2.1 | 9 | 0 | 25-32 | 85 | 24.5 | Berawan |
| Mataram | 1.7 | 15 | 0 | 24-32 | 81 | 27.8 | Cerah |
| Surabaya | 1.5 | 9 | 0 | 24-36 | 78 | 11.5 | Berawan |
| Padang | 1.4 | 21 | 0 | 25-28 | 83 | 8.0 | Berawan |
| Manado | 0.9 | 9 | 0 | 24-35 | 78 | 8.2 | Cerah |
| Jayapura | 0.6 | 6 | 0 | 23-26 | 89 | 11.2 | Udara Kabur |
| Kupang | 0.2 | 3 | 0 | 25-34 | 70 | 18.1 | Cerah |
| Makassar | 0.0 | 0 | 0 | 26-35 | 79 | 15.8 | Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 104 | 31.2 | 12 |
| Udara Kabur | 80 | 24.0 | 9 |
| Cerah | 66 | 19.8 | 11 |
| Cerah Berawan | 62 | 18.6 | 14 |
| Hujan Ringan | 19 | 5.7 | 11 |
| Kabut/Asap | 2 | 0.6 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 28 Oct 14:00: suhu 34 C (Cerah Berawan)
- **Kupang** 27 Oct 14:00: suhu 34 C (Cerah)
- **Semarang** 26 Oct 12:00: suhu 34 C (Cerah Berawan)
- **Makassar** 27 Oct 14:00: suhu 35 C (Berawan)
- **Makassar** 28 Oct 14:00: suhu 35 C (Cerah)
- **Surabaya** 26 Oct 12:00: suhu 36 C (Berawan)
- **Manado** 26 Oct 13:00: suhu 35 C (Cerah)
- **Kupang** 28 Oct 11:00: suhu 34 C (Cerah Berawan)
- **Kupang** 26 Oct 14:00: suhu 34 C (Berawan)
- **Makassar** 26 Oct 14:00: suhu 34 C (Berawan)
- **Manado** 27 Oct 13:00: suhu 34 C (Cerah)

## Gambar

![total curah hujan 51 jam per kota](figures/01_curah_hujan_kota.png)

![peta panas curah hujan harian](figures/02_heatmap_harian.png)

![rentang suhu dan suhu terasa](figures/03_rentang_suhu.png)

![profil hujan kota terbasah](figures/04_profil_hujan_terbasah.png)

## Catatan metode

- Setiap slot mewakili 3 jam. `jam_hujan` = jumlah slot dengan curah hujan > 0 dikali 3.
- Suhu terasa memakai apparent temperature Steadman: `AT = Ta + 0.33e - 0.70ws - 4.00`, dengan `e` tekanan uap air dari suhu dan kelembapan.
- Kategori hujan per slot: kering (< 0,1 mm), ringan (< 5 mm), sedang (< 20 mm), lebat (< 50 mm), sangat lebat.
- Prakiraan BMKG adalah keluaran model, bukan observasi. Angka bisa berubah setiap kali pipeline dijalankan.
