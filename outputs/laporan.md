# Prakiraan Cuaca Indonesia

Analisis 19 kota, 416 slot prakiraan 3 jam (24 Okt 2026 sampai 26 Okt 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-10-23 23:53 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 28.2 mm dalam 66 jam.
- Paling kering: **Kupang** dengan 0.3 mm.
- Suhu tertinggi: **Surabaya** 36 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 16.0 C (selisih harian rata-rata 7.5 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 28.2 | 51 | 0 | 20-29 | 83 | 8.8 | Hujan Ringan |
| Medan | 22.3 | 48 | 0 | 24-30 | 91 | 9.3 | Berawan |
| Pekanbaru | 15.3 | 27 | 0 | 24-30 | 92 | 10.6 | Hujan Ringan |
| Palembang | 10.5 | 51 | 0 | 24-35 | 82 | 9.1 | Udara Kabur |
| Padang | 9.7 | 60 | 0 | 25-27 | 85 | 10.4 | Berawan |
| Banda Aceh | 8.4 | 30 | 0 | 24-29 | 84 | 18.6 | Berawan |
| Denpasar | 7.1 | 24 | 0 | 25-34 | 81 | 18.4 | Cerah Berawan |
| Pontianak | 6.1 | 36 | 0 | 23-32 | 88 | 10.7 | Udara Kabur |
| Semarang | 5.5 | 27 | 0 | 25-35 | 73 | 9.0 | Berawan |
| Mataram | 4.1 | 33 | 0 | 24-35 | 77 | 22.3 | Berawan |
| Jakarta Pusat | 3.6 | 51 | 0 | 25-32 | 76 | 10.5 | Berawan |
| Balikpapan | 2.0 | 27 | 0 | 26-30 | 82 | 15.7 | Udara Kabur |
| Bandar Lampung | 1.7 | 24 | 0 | 24-31 | 75 | 21.6 | Berawan |
| Makassar | 1.3 | 27 | 0 | 26-31 | 79 | 21.6 | Berawan |
| Surabaya | 1.2 | 9 | 0 | 26-36 | 59 | 15.5 | Berawan |
| Manado | 0.9 | 15 | 0 | 23-34 | 74 | 10.4 | Udara Kabur |
| Ambon | 0.6 | 6 | 0 | 25-32 | 87 | 11.5 | Udara Kabur |
| Jayapura | 0.3 | 6 | 0 | 23-29 | 86 | 13.8 | Udara Kabur |
| Kupang | 0.3 | 9 | 0 | 24-32 | 70 | 27.8 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 159 | 38.2 | 16 |
| Udara Kabur | 112 | 26.9 | 9 |
| Cerah Berawan | 67 | 16.1 | 14 |
| Hujan Ringan | 42 | 10.1 | 10 |
| Cerah | 34 | 8.2 | 9 |
| Hujan Sedang | 2 | 0.5 | 2 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Mataram** 24 Oct 14:00: suhu 34 C (Cerah)
- **Denpasar** 25 Oct 14:00: suhu 34 C (Hujan Ringan)
- **Denpasar** 24 Oct 14:00: suhu 34 C (Cerah Berawan)
- **Surabaya** 24 Oct 13:00: suhu 36 C (Cerah)
- **Surabaya** 25 Oct 13:00: suhu 35 C (Berawan)
- **Mataram** 26 Oct 11:00: suhu 34 C (Hujan Ringan)
- **Surabaya** 26 Oct 13:00: suhu 35 C (Berawan)
- **Mataram** 25 Oct 14:00: suhu 35 C (Berawan)
- **Mataram** 26 Oct 14:00: suhu 35 C (Hujan Ringan)
- **Palembang** 24 Oct 16:00: suhu 34 C (Hujan Ringan)
- **Semarang** 24 Oct 13:00: suhu 35 C (Berawan)
- **Manado** 24 Oct 14:00: suhu 34 C (Udara Kabur)

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
