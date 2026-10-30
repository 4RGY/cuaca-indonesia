# Prakiraan Cuaca Indonesia

Analisis 19 kota, 407 slot prakiraan 3 jam (30 Okt 2026 sampai 1 Nov 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-10-30 01:08 UTC.

## Angka kunci

- Paling basah: **Banda Aceh** dengan 16.9 mm dalam 63 jam.
- Paling kering: **Surabaya** dengan 1.3 mm.
- Suhu tertinggi: **Kupang** 35 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 15.0 C (selisih harian rata-rata 7.5 C).
- Kota tanpa hujan sama sekali: 0 dari 19.

## Ringkasan per kota

| Kota | Hujan 63 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Banda Aceh | 16.9 | 45 | 0 | 24-29 | 87 | 9.7 | Cerah Berawan |
| Padang | 14.3 | 45 | 0 | 25-29 | 84 | 11.7 | Cerah |
| Denpasar | 11.0 | 18 | 0 | 25-32 | 86 | 20.4 | Cerah Berawan |
| Pontianak | 8.2 | 33 | 0 | 23-31 | 89 | 9.9 | Cerah |
| Mataram | 7.8 | 33 | 0 | 24-31 | 84 | 18.3 | Cerah |
| Bandung | 7.5 | 6 | 0 | 20-32 | 83 | 12.6 | Cerah |
| Medan | 6.5 | 39 | 0 | 24-31 | 87 | 8.2 | Cerah |
| Ambon | 6.2 | 30 | 0 | 24-29 | 88 | 12.0 | Udara Kabur |
| Bandar Lampung | 5.4 | 51 | 0 | 23-31 | 83 | 16.4 | Cerah Berawan |
| Semarang | 5.2 | 30 | 0 | 25-32 | 79 | 9.0 | Cerah |
| Palembang | 5.1 | 36 | 0 | 24-32 | 83 | 11.7 | Cerah |
| Kupang | 4.3 | 27 | 0 | 25-35 | 73 | 13.3 | Cerah |
| Manado | 4.2 | 36 | 0 | 23-32 | 79 | 11.5 | Cerah Berawan |
| Jakarta Pusat | 3.9 | 30 | 0 | 24-31 | 82 | 9.9 | Cerah |
| Balikpapan | 3.0 | 24 | 0 | 24-30 | 82 | 13.6 | Udara Kabur |
| Jayapura | 2.9 | 30 | 0 | 22-32 | 86 | 14.3 | Udara Kabur |
| Pekanbaru | 2.4 | 6 | 0 | 23-31 | 85 | 9.1 | Berawan |
| Makassar | 1.6 | 30 | 0 | 27-30 | 76 | 21.8 | Cerah |
| Surabaya | 1.3 | 9 | 0 | 24-35 | 69 | 27.8 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 155 | 38.1 | 17 |
| Cerah Berawan | 103 | 25.3 | 16 |
| Berawan | 58 | 14.3 | 16 |
| Udara Kabur | 57 | 14.0 | 7 |
| Hujan Ringan | 32 | 7.9 | 14 |
| Petir | 2 | 0.5 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Surabaya** 31 Oct 14:00: suhu 34 C (Cerah)
- **Surabaya** 01 Nov 11:00: suhu 34 C (Cerah)
- **Surabaya** 01 Nov 14:00: suhu 34 C (Cerah Berawan)
- **Kupang** 31 Oct 15:00: suhu 35 C (Cerah)
- **Kupang** 30 Oct 15:00: suhu 34 C (Cerah)
- **Surabaya** 30 Oct 11:00: suhu 35 C (Berawan)
- **Kupang** 30 Oct 12:00: suhu 34 C (Cerah)
- **Surabaya** 31 Oct 11:00: suhu 34 C (Cerah)

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
