# Cuaca Indonesia

Analisis prakiraan cuaca BMKG untuk 19 kota, dari Banda Aceh sampai Jayapura. Satu perintah
mengambil data resmi BMKG, menghitung ringkasan per kota, menggambar empat grafik, dan menulis
laporan markdown. Semua angka di laporan dihitung ulang saat pipeline jalan, tidak ada yang
ditempel manual.

Data pada contoh di bawah diambil **20 Oktober 2026, 18:30 UTC**.

## Kenapa proyek ini

Prakiraan cuaca BMKG berbentuk data per kelurahan dengan slot 3 jam. Bentuk mentahnya tidak enak
dibaca: ratusan objek bersarang, satuan campur, dan tiap kota punya kode wilayah sendiri.
Proyek ini merapikan itu jadi tabel panjang (`prakiraan.csv`) lalu menjawab pertanyaan yang
sering muncul: kota mana yang bakal paling basah, di mana suhu ekstrem, dan bagaimana sebaran
kondisi cuaca secara nasional.

## Hasil sekali jalan

Ambil contoh nyata dari `outputs/laporan.md` (19 kota, 375 slot):

| Pertanyaan | Jawaban |
|---|---|
| Paling basah | **Medan**, 19,6 mm dalam 60 jam |
| Paling kering | **Surabaya**, 0,0 mm |
| Suhu tertinggi | **Palembang**, 37 C |
| Suhu terendah | **Bandung**, 20 C |
| Rentang suhu antar kota | 17 C |
| Kota tanpa hujan | 2 dari 19 |
| Slot lewat ambang | 12 slot (hujan lebat, angin >= 30 km/jam, atau suhu >= 34 C) |
| Kondisi didominasi | Cerah 44%, **Udara Kabur 31%** (10 kota), Berawan 10% |

Satu temuan yang khas Indonesia: nyaris sepertiga slot prakiraan berstatus **Udara Kabur**,
bukan hujan atau cerah. Itu asap/kabut yang menutup jarak pandang, dan muncul di 10 kota
sekaligus pada periode yang sama.

## Gambar

![Total curah hujan per kota](outputs/figures/01_curah_hujan_kota.png)

![Peta panas curah hujan harian](outputs/figures/02_heatmap_harian.png)

![Rentang suhu dan suhu terasa](outputs/figures/03_rentang_suhu.png)

![Profil hujan kota terbasah](outputs/figures/04_profil_hujan_terbasah.png)

## Isi laporan

`outputs/laporan.md` berisi:

1. Angka kunci nasional (terbasah, terkering, terpanas, terdingin, rentang suhu).
2. Tabel 19 kota: curah hujan, jam hujan, slot hujan lebat, rentang suhu, kelembapan,
   angin maksimum, kondisi dominan.
3. Sebaran kondisi cuaca yang diprediksi, dihitung per slot.
4. Peringatan dini: slot yang melewati ambang hujan lebat, angin kencang, atau suhu ekstrem.
5. Catatan metode, termasuk rumus suhu terasa.

Selain laporan, pipeline menulis `prakiraan.csv` (satu baris per kota per slot),
`ringkasan_kota.csv`, dan `ringkasan.json`.

## Cara jalan

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

python scripts/resolve_wilayah.py   # sekali saja, mengisi data/kota.json
python -m cuaca_indonesia.cli       # ambil BMKG -> analisis -> grafik -> laporan
python -m pytest                    # 16 tes, tanpa jaringan
```

Opsi CLI:

```bash
python -m cuaca_indonesia.cli --horizon 48 --outdir outputs --tanpa-cache
```

## Kota yang dipantau

Banda Aceh, Medan, Padang, Pekanbaru, Palembang, Bandar Lampung, Jakarta Pusat, Bandung,
Semarang, Surabaya, Denpasar, Mataram, Kupang, Pontianak, Balikpapan, Manado, Makassar,
Ambon, Jayapura.

`data/kota.json` menyimpan kode adm4 tiap kota. Kode diambil dari dataset wilayah administrasi
(BPS/Kemendagri) lalu **diverifikasi satu per satu ke API BMKG**: respons BMKG harus menyebut
kota dan kecamatan yang sama. 19 dari 19 kota lolos verifikasi.

## Catatan teknis yang bikin proyek ini tidak sekadar `requests.get`

Dua hal ini bikin pipeline gagal kalau tidak ditangani, jadi ditulis eksplisit di kode:

1. **Kode wilayah harus bertitik.** `3171021001` dibalas `502`, `31.71.02.1001` dibalas `200`.
   Fungsi `format_adm4()` menormalkan kode sebelum request.
2. **Cloudflare menolak fingerprint TLS `requests`.** Dengan kode yang benar pun `requests`
   kena `403`, sementara `curl` lolos. Solusinya `curl_cffi` dengan impersonasi browser.

Detail lain: setiap respons di-cache di `data/cache/`, ada jeda 1 detik antar kota, retry
berjenjang 3/6/9/12 detik, dan kota yang gagal tidak mematikan seluruh pipeline.

## Metode

- **Suhu terasa** memakai apparent temperature Steadman (versi operasional BoM):
  `AT = Ta + 0,33e - 0,70ws - 4,00`, dengan `e` tekanan uap air (hPa) dari suhu dan kelembapan,
  `ws` kecepatan angin dalam m/s.
- **Kategori hujan per slot 3 jam**: kering (< 0,1 mm), ringan (< 5 mm), sedang (< 20 mm),
  lebat (< 50 mm), sangat lebat (>= 50 mm).
- **Jam hujan** = jumlah slot dengan curah hujan > 0 dikali 3. Slot BMKG tidak selalu tepat
  3 jam di setiap kota, karena itu laporan juga menampilkan jumlah slot.
- Prakiraan adalah keluaran model, bukan observasi. Angka berubah setiap kali pipeline jalan.

## Struktur

```
cuaca-indonesia/
  src/cuaca_indonesia/
    fetch.py      ambil API BMKG (curl_cffi, cache, retry, format adm4)
    parse.py      payload bersarang -> tabel panjang + suhu terasa
    analysis.py   agregasi per kota, per hari, peringatan, kontras suhu
    charts.py     empat grafik matplotlib
    report.py     laporan markdown
    cli.py        orkestrator
  scripts/resolve_wilayah.py   kode wilayah + verifikasi BMKG
  data/kota.json               19 kota terverifikasi
  tests/test_cuaca.py          16 tes offline
  outputs/                     laporan, csv, grafik
```

## Lisensi

MIT. Data cuaca milik BMKG, dipakai sesuai ketentuan data terbuka BMKG.
