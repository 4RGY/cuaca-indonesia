# Prakiraan Cuaca Indonesia

Analisis 19 kota, 413 slot prakiraan 3 jam (23 Okt 2026 sampai 25 Okt 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-10-23 00:01 UTC.

## Angka kunci

- Paling basah: **Padang** dengan 18.1 mm dalam 66 jam.
- Paling kering: **Surabaya** dengan 0.0 mm.
- Suhu tertinggi: **Surabaya** 36 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 16.0 C (selisih harian rata-rata 7.5 C).
- Kota tanpa hujan sama sekali: 2 dari 19.

## Ringkasan per kota

| Kota | Hujan 66 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Padang | 18.1 | 63 | 0 | 25-28 | 86 | 10.2 | Udara Kabur |
| Medan | 16.0 | 36 | 0 | 23-31 | 92 | 7.6 | Cerah Berawan |
| Banda Aceh | 12.8 | 54 | 0 | 24-29 | 87 | 14.2 | Berawan |
| Bandung | 12.0 | 48 | 0 | 20-31 | 73 | 10.0 | Berawan |
| Palembang | 11.8 | 51 | 0 | 24-35 | 78 | 10.9 | Udara Kabur |
| Pekanbaru | 10.6 | 42 | 0 | 24-31 | 88 | 7.6 | Berawan |
| Pontianak | 4.9 | 30 | 0 | 24-32 | 88 | 8.1 | Udara Kabur |
| Jayapura | 4.3 | 36 | 0 | 23-28 | 85 | 11.9 | Udara Kabur |
| Denpasar | 3.5 | 48 | 0 | 24-33 | 80 | 18.5 | Cerah Berawan |
| Mataram | 2.9 | 30 | 0 | 24-32 | 77 | 17.4 | Berawan |
| Semarang | 2.5 | 24 | 0 | 25-35 | 65 | 18.5 | Berawan |
| Jakarta Pusat | 2.4 | 27 | 0 | 24-33 | 77 | 10.0 | Berawan |
| Ambon | 2.1 | 30 | 0 | 24-29 | 85 | 12.3 | Udara Kabur |
| Balikpapan | 1.6 | 21 | 0 | 26-30 | 78 | 14.7 | Berawan |
| Bandar Lampung | 1.5 | 24 | 0 | 24-31 | 74 | 22.2 | Cerah Berawan |
| Kupang | 0.4 | 6 | 0 | 24-32 | 70 | 15.2 | Cerah |
| Makassar | 0.2 | 6 | 0 | 27-34 | 74 | 20.4 | Cerah |
| Manado | 0.0 | 0 | 0 | 24-32 | 71 | 12.0 | Cerah |
| Surabaya | 0.0 | 0 | 0 | 26-36 | 54 | 39.7 | Berawan |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Berawan | 113 | 27.4 | 15 |
| Udara Kabur | 102 | 24.7 | 10 |
| Cerah | 90 | 21.8 | 12 |
| Cerah Berawan | 80 | 19.4 | 16 |
| Hujan Ringan | 24 | 5.8 | 8 |
| Hujan Petir | 3 | 0.7 | 2 |
| Petir | 1 | 0.2 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Surabaya** 23 Oct 13:00: angin 40 km/jam, suhu 36 C (Cerah)
- **Makassar** 23 Oct 15:00: suhu 34 C (Cerah)
- **Semarang** 23 Oct 10:00: suhu 34 C (Cerah)
- **Semarang** 23 Oct 13:00: suhu 35 C (Cerah)
- **Semarang** 24 Oct 13:00: suhu 35 C (Cerah)
- **Semarang** 25 Oct 13:00: suhu 34 C (Berawan)
- **Surabaya** 25 Oct 13:00: suhu 36 C (Berawan)
- **Surabaya** 25 Oct 16:00: suhu 34 C (Berawan)
- **Surabaya** 24 Oct 13:00: suhu 35 C (Cerah Berawan)
- **Surabaya** 24 Oct 16:00: suhu 34 C (Cerah)
- **Palembang** 23 Oct 16:00: suhu 35 C (Udara Kabur)
- **Palembang** 23 Oct 13:00: suhu 35 C (Udara Kabur)

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
