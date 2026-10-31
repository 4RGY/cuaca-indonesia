# Prakiraan Cuaca Indonesia

Analisis 19 kota, 410 slot prakiraan 3 jam (31 Okt 2026 sampai 2 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-10-31 00:52 UTC.

## Angka kunci

- Paling basah: **Bandung** dengan 13.4 mm dalam 66 jam.
- Paling kering: **Makassar** dengan 1.2 mm.
- Suhu tertinggi: **Kupang** 36 C.
- Suhu terendah: **Bandung** 19 C.
- Rentang suhu antar kota: 17.0 C (selisih harian rata-rata 7.2 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Bandung | 13.4 | 30 | 0 | 19-28 | 83 | 9.7 | Cerah |
| Palembang | 9.1 | 60 | 0 | 24-33 | 85 | 10.2 | Udara Kabur |
| Banda Aceh | 8.1 | 45 | 0 | 24-29 | 87 | 12.6 | Cerah |
| Medan | 8.0 | 45 | 0 | 23-30 | 88 | 9.7 | Cerah |
| Manado | 7.4 | 33 | 0 | 24-31 | 85 | 9.5 | Cerah Berawan |
| Pekanbaru | 6.9 | 54 | 0 | 23-31 | 88 | 8.8 | Cerah |
| Padang | 6.9 | 39 | 0 | 25-28 | 83 | 9.2 | Cerah |
| Ambon | 6.8 | 27 | 0 | 23-30 | 88 | 12.4 | Udara Kabur |
| Semarang | 6.7 | 39 | 0 | 25-35 | 79 | 18.5 | Cerah |
| Pontianak | 6.3 | 33 | 0 | 23-32 | 89 | 9.4 | Berawan |
| Bandar Lampung | 6.3 | 57 | 0 | 24-30 | 83 | 15.5 | Cerah |
| Denpasar | 6.0 | 33 | 0 | 23-30 | 86 | 18.0 | Cerah |
| Mataram | 5.0 | 33 | 0 | 24-33 | 82 | 27.8 | Cerah Berawan |
| Jakarta Pusat | 5.0 | 51 | 0 | 25-32 | 79 | 9.7 | Cerah |
| Balikpapan | 3.9 | 30 | 0 | 24-29 | 81 | 13.1 | Cerah |
| Jayapura | 3.0 | 33 | 0 | 23-28 | 85 | 11.3 | Cerah Berawan |
| Kupang | 2.5 | 24 | 0 | 25-36 | 72 | 37.1 | Cerah |
| Surabaya | 1.3 | 30 | 0 | 25-35 | 68 | 13.1 | Cerah |
| Makassar | 1.2 | 27 | 0 | 27-30 | 76 | 15.9 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 152 | 37.1 | 18 |
| Cerah Berawan | 91 | 22.2 | 18 |
| Berawan | 88 | 21.5 | 17 |
| Udara Kabur | 47 | 11.5 | 9 |
| Hujan Ringan | 31 | 7.6 | 14 |
| Petir | 1 | 0.2 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 01 Nov 15:00: angin 37 km/jam, suhu 36 C (Cerah Berawan)
- **Kupang** 02 Nov 12:00: angin 37 km/jam, suhu 35 C (Cerah Berawan)
- **Kupang** 31 Oct 15:00: angin 37 km/jam, suhu 36 C (Cerah)
- **Kupang** 02 Nov 15:00: angin 37 km/jam, suhu 35 C (Cerah Berawan)
- **Kupang** 31 Oct 18:00: angin 37 km/jam (Cerah)
- **Kupang** 01 Nov 18:00: angin 37 km/jam (Cerah Berawan)
- **Semarang** 02 Nov 11:00: suhu 35 C (Cerah)
- **Surabaya** 02 Nov 14:00: suhu 34 C (Cerah)
- **Surabaya** 02 Nov 11:00: suhu 34 C (Cerah Berawan)
- **Surabaya** 01 Nov 14:00: suhu 34 C (Cerah Berawan)
- **Surabaya** 31 Oct 14:00: suhu 35 C (Cerah)
- **Kupang** 01 Nov 12:00: suhu 34 C (Cerah)

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
