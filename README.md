# PhisDetector

**PhisDetector** (nama sebelumnya: PhishGuard) adalah CLI tool sederhana untuk mendeteksi indikasi *homograph attack* pada URL — teknik phishing di mana penyerang menggunakan karakter non-ASCII (mis. Cyrillic, Greek, atau karakter IDN lain) yang tampak mirip dengan huruf Latin untuk menyamarkan domain palsu.

---

## Fitur

- **Validasi URL** — memastikan input berupa URL yang valid sebelum diproses (`validators`).
- **Ekstraksi Domain** — mengambil domain murni dari URL menggunakan `tldextract`.
- **Decode Punycode/IDN** — mendekode domain yang dienkode dalam bentuk punycode (`xn--...`) menggunakan `idna`.
- **Analisis Karakter** — memeriksa setiap karakter dalam domain, menampilkan code point Unicode dan nama resminya.
- **Deteksi Non-ASCII** — menandai domain sebagai **"Suspicious"** jika mengandung karakter dengan code point di atas 127 (indikasi potensi homograph attack), atau **"Safe"** jika seluruh karakter ASCII standar.

---

## Tech Stack

- **Bahasa:** Python
- **Library:** `tldextract`, `idna`, `validators`, `unicodedata` (built-in)
- **Interface:** CLI interaktif

---

## Instalasi

```bash
git clone https://github.com/Lincosin/PishDetector.git
cd PishDetector

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install tldextract idna validators
```

> Catatan: repo belum memiliki `requirements.txt` — silakan buat dari daftar di atas, atau jalankan `pip freeze > requirements.txt` setelah instalasi.

---

## Cara Pakai

Jalankan langsung, lalu masukkan URL saat diminta:

```bash
python main.py
```

Contoh sesi:

```
==================================================
Homograph Detector v1
==================================================

Input URL : http://xn--pypal-4ve.com

========== RESULT ==========
Domain : paypal.com
Status : Suspicious

Character Analysis
----------------------------------------
Character : p
Unicode : U+0070
Name : LATIN SMALL LETTER P
----------------------------------------
Character : а
Unicode : U+0430
Name : CYRILLIC SMALL LETTER A
...
```

---

## Struktur Proyek

```
PishDetector/
├── main.py          # Entry point CLI — alur input, validasi, analisis, output
├── validator.py      # Validasi format URL
├── parser.py         # Ekstraksi domain + decode punycode
├── detector.py        # Analisis karakter & penentuan status Safe/Suspicious
├── report.py          # Format tampilan hasil ke terminal
└── README.md
```

---

## Roadmap

- [x] CLI dasar: validasi URL → ekstraksi domain → analisis karakter → laporan
- [x] Deteksi punycode/IDN
- [x] Deteksi karakter non-ASCII sederhana
- [ ] Homoglyph/confusables detection yang lebih presisi (bukan sekadar cek `ord(char) > 127`)
- [ ] Typosquatting check (kemiripan dengan domain populer)
- [ ] Sistem skor risiko (0–100) sebagai pengganti status biner Safe/Suspicious
- [ ] Unit test (pytest)
- [ ] `requirements.txt`
- [ ] Integrasi backend FastAPI
- [ ] Integrasi reputation API (VirusTotal, Google Safe Browsing)

---

## Kontak
**I Putu Willy Nugraha**
🔗 [linkedin.com/in/willy-nugraha](https://linkedin.com/in/willy-nugraha)
