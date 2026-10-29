# Prakiraan Cuaca Indonesia

Analisis 19 kota, 409 slot prakiraan 3 jam (29 Okt 2026 sampai 31 Okt 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-10-29 01:03 UTC.

## Angka kunci

- Paling basah: **Medan** dengan 16.0 mm dalam 66 jam.
- Paling kering: **Jayapura** dengan 0.8 mm.
- Suhu tertinggi: **Kupang** 34 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 15.0 C (selisih harian rata-rata 7.0 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Medan | 16.0 | 30 | 0 | 24-30 | 89 | 9.8 | Berawan |
| Pontianak | 14.9 | 39 | 0 | 23-31 | 91 | 9.8 | Berawan |
| Bandung | 14.7 | 18 | 0 | 19-32 | 85 | 10.3 | Cerah |
| Pekanbaru | 11.4 | 18 | 0 | 23-31 | 87 | 9.2 | Cerah Berawan |
| Palembang | 10.2 | 39 | 0 | 24-32 | 86 | 7.5 | Berawan |
| Bandar Lampung | 9.9 | 33 | 0 | 24-31 | 86 | 12.1 | Cerah |
| Semarang | 6.8 | 42 | 0 | 24-32 | 81 | 11.7 | Cerah |
| Padang | 6.4 | 51 | 0 | 24-28 | 85 | 8.2 | Berawan |
| Jakarta Pusat | 6.3 | 33 | 0 | 25-31 | 84 | 7.1 | Cerah |
| Banda Aceh | 5.8 | 42 | 0 | 24-29 | 87 | 14.3 | Berawan |
| Mataram | 5.7 | 33 | 0 | 22-32 | 81 | 18.5 | Cerah |
| Denpasar | 4.0 | 51 | 0 | 24-29 | 85 | 17.6 | Cerah |
| Kupang | 3.5 | 24 | 0 | 25-34 | 73 | 27.8 | Cerah |
| Surabaya | 3.3 | 24 | 0 | 24-34 | 73 | 12.1 | Cerah |
| Manado | 3.0 | 18 | 0 | 25-32 | 74 | 9.4 | Cerah |
| Balikpapan | 1.9 | 33 | 0 | 25-30 | 80 | 16.3 | Cerah |
| Ambon | 1.2 | 6 | 0 | 24-28 | 86 | 13.6 | Udara Kabur |
| Makassar | 1.0 | 18 | 0 | 27-32 | 71 | 18.5 | Cerah |
| Jayapura | 0.8 | 15 | 0 | 24-29 | 81 | 14.6 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 171 | 41.8 | 17 |
| Berawan | 84 | 20.5 | 15 |
| Cerah Berawan | 80 | 19.6 | 19 |
| Hujan Ringan | 37 | 9.0 | 12 |
| Udara Kabur | 33 | 8.1 | 9 |
| Hujan Petir | 1 | 0.2 | 1 |
| Hujan Sedang | 1 | 0.2 | 1 |
| Kabut/Asap | 1 | 0.2 | 1 |
| Petir | 1 | 0.2 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 29 Oct 13:00: suhu 34 C (Cerah)
- **Surabaya** 31 Oct 11:00: suhu 34 C (Cerah)
- **Surabaya** 31 Oct 14:00: suhu 34 C (Cerah)
- **Surabaya** 29 Oct 14:00: suhu 34 C (Cerah)

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
