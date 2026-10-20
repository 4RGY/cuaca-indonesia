# Prakiraan Cuaca Indonesia

Analisis 19 kota, 375 slot prakiraan 3 jam (20 Okt 2026 sampai 22 Okt 2026). Sumber: API prakiraan cuaca BMKG. Dibuat 2026-10-20 18:41 UTC.

## Angka kunci

- Paling basah: **Medan** dengan 19.6 mm dalam 60 jam.
- Paling kering: **Surabaya** dengan 0.0 mm.
- Suhu tertinggi: **Palembang** 37 C.
- Suhu terendah: **Bandung** 20 C.
- Rentang suhu antar kota: 17.0 C (selisih harian rata-rata 8.2 C).
- Kota tanpa hujan sama sekali: 2 dari 19.

## Ringkasan per kota

| Kota | Hujan 60 jam (mm) | Jam hujan | Slot lebat | Suhu (C) | RH (%) | Angin maks (km/jam) | Kondisi dominan |
|---|---|---|---|---|---|---|---|
| Medan | 19.6 | 36 | 0 | 23-31 | 89 | 9.8 | Berawan |
| Pontianak | 15.4 | 36 | 0 | 24-34 | 91 | 9.5 | Udara Kabur |
| Banda Aceh | 12.8 | 48 | 0 | 24-30 | 87 | 15.6 | Berawan |
| Padang | 4.5 | 45 | 0 | 25-30 | 85 | 7.6 | Cerah |
| Jakarta Pusat | 3.8 | 24 | 0 | 26-33 | 69 | 12.2 | Cerah |
| Ambon | 1.8 | 36 | 0 | 24-30 | 83 | 13.5 | Udara Kabur |
| Kupang | 1.4 | 12 | 0 | 24-33 | 64 | 37.0 | Udara Kabur |
| Bandar Lampung | 1.1 | 21 | 0 | 23-34 | 75 | 16.5 | Cerah |
| Semarang | 1.0 | 18 | 0 | 26-36 | 64 | 12.1 | Cerah |
| Mataram | 0.8 | 12 | 0 | 23-31 | 76 | 27.8 | Cerah |
| Balikpapan | 0.7 | 15 | 0 | 27-31 | 77 | 21.7 | Udara Kabur |
| Pekanbaru | 0.6 | 6 | 0 | 24-32 | 84 | 11.1 | Udara Kabur |
| Jayapura | 0.4 | 12 | 0 | 23-29 | 83 | 13.8 | Udara Kabur |
| Palembang | 0.3 | 9 | 0 | 25-37 | 59 | 16.7 | Udara Kabur |
| Manado | 0.3 | 6 | 0 | 24-32 | 74 | 9.8 | Cerah |
| Makassar | 0.2 | 6 | 0 | 25-32 | 65 | 27.7 | Cerah |
| Denpasar | 0.1 | 3 | 0 | 24-31 | 76 | 17.8 | Cerah |
| Bandung | 0.0 | 0 | 0 | 20-32 | 58 | 11.0 | Cerah |
| Surabaya | 0.0 | 0 | 0 | 26-37 | 56 | 33.0 | Cerah |

## Kondisi yang diprediksi

| Kondisi | Slot | Porsi (%) | Jumlah kota |
|---|---|---|---|
| Cerah | 165 | 44.0 | 15 |
| Udara Kabur | 116 | 30.9 | 10 |
| Cerah Berawan | 41 | 10.9 | 14 |
| Berawan | 36 | 9.6 | 11 |
| Hujan Ringan | 12 | 3.2 | 3 |
| Hujan Sedang | 2 | 0.5 | 2 |
| Hujan Petir | 1 | 0.3 | 1 |
| Kabut/Asap | 1 | 0.3 | 1 |
| Petir | 1 | 0.3 | 1 |

## Peringatan dini

Slot yang melewati ambang hujan lebat (>= 20 mm/3 jam), angin kencang (>= 30 km/jam), atau suhu ekstrem (>= 34 C):

- **Kupang** 21 Oct 15:00: angin 37 km/jam (Udara Kabur)
- **Kupang** 21 Oct 18:00: angin 37 km/jam (Udara Kabur)
- **Surabaya** 21 Oct 14:00: angin 33 km/jam, suhu 37 C (Cerah)
- **Surabaya** 20 Oct 14:00: angin 32 km/jam, suhu 37 C (Cerah)
- **Surabaya** 22 Oct 11:00: angin 31 km/jam, suhu 36 C (Cerah)
- **Surabaya** 22 Oct 14:00: angin 31 km/jam, suhu 36 C (Cerah)
- **Palembang** 21 Oct 17:00: suhu 34 C (Udara Kabur)
- **Palembang** 22 Oct 17:00: suhu 35 C (Udara Kabur)
- **Pontianak** 21 Oct 14:00: suhu 34 C (Hujan Sedang)
- **Bandar Lampung** 22 Oct 11:00: suhu 34 C (Cerah Berawan)
- **Bandar Lampung** 20 Oct 14:00: suhu 34 C (Cerah)
- **Semarang** 22 Oct 11:00: suhu 34 C (Cerah)

## Gambar

![total curah hujan 60 jam per kota](figures/01_curah_hujan_kota.png)

![peta panas curah hujan harian](figures/02_heatmap_harian.png)

![rentang suhu dan suhu terasa](figures/03_rentang_suhu.png)

![profil hujan kota terbasah](figures/04_profil_hujan_terbasah.png)

## Catatan metode

- Setiap slot mewakili 3 jam. `jam_hujan` = jumlah slot dengan curah hujan > 0 dikali 3.
- Suhu terasa memakai apparent temperature Steadman: `AT = Ta + 0.33e - 0.70ws - 4.00`, dengan `e` tekanan uap air dari suhu dan kelembapan.
- Kategori hujan per slot: kering (< 0,1 mm), ringan (< 5 mm), sedang (< 20 mm), lebat (< 50 mm), sangat lebat.
- Prakiraan BMKG adalah keluaran model, bukan observasi. Angka bisa berubah setiap kali pipeline dijalankan.
