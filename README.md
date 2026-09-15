# PhisDetector

**PhisDetector** adalah tool pendeteksi phishing berbasis analisis URL, dibangun untuk mengidentifikasi tautan berbahaya sebelum diakses pengguna. Proyek ini menggabungkan beberapa teknik deteksi klasik (homograph, punycode/IDN, typosquatting) dengan sistem scoring risiko sederhana.

> Sebelumnya dikenal sebagai **PhishGuard**.

---

## Fitur Utama

- **Homograph Detection** — mendeteksi karakter yang secara visual mirip (mis. Cyrillic vs Latin) yang sering dipakai untuk menyamarkan domain palsu.
- **Punycode / IDN Detection** — mengenali domain internationalized (xn--) yang berpotensi disalahgunakan.
- **Typosquatting Check** — mendeteksi domain yang menyerupai domain populer dengan sedikit perbedaan ejaan.
- **Risk Scoring System (0–100)** — menggabungkan seluruh sinyal deteksi menjadi satu skor risiko yang mudah diinterpretasikan.
- **Unit Tested** — 16 unit test untuk memastikan setiap modul deteksi berjalan sesuai ekspektasi.

---

## Tech Stack

- **Bahasa:** Python
- **Library:** `unicodedata`, `idna`, `confusable_homoglyphs` (atau library confusables sejenis)
- **Testing:** `pytest` / `unittest`
- **Interface saat ini:** CLI (Command Line Interface)
- **Rencana pengembangan:** REST API dengan **FastAPI**, terintegrasi dengan reputation API pihak ketiga (VirusTotal, Google Safe Browsing)

---

## Instalasi

```bash
# Clone repository
git clone https://github.com/<username>/phisdetector.git
cd phisdetector

# (Opsional) buat virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

```

---

## Cara Pakai

```bash
python phisdetector.py --url "http://contoh-domain-mencurigakan.com"
```

Contoh output:

```
URL      : http://contoh-domain-mencurigakan.com
Risk Score : 78/100
Detected Issues:
  - Typosquatting terhadap domain populer
  - Karakter IDN terdeteksi
Status   :  Berisiko Tinggi
```

> Sesuaikan nama file, argumen CLI, dan contoh output di atas dengan implementasi aktual kamu.

---

## Menjalankan Test

```bash
pytest tests/
```

Saat ini terdapat **16 unit test** yang mencakup modul homograph detection, punycode detection, typosquatting check, dan scoring engine.

---

## Struktur Proyek

```
phisdetector/
├── phisdetector.py          # Entry point CLI
├── detectors/
│   ├── homograph.py         # Deteksi karakter homoglyph
│   ├── punycode.py          # Deteksi domain IDN/punycode
│   └── typosquatting.py     # Deteksi kemiripan domain
├── scoring.py                # Logika risk scoring (0-100)
├── tests/
│   └── test_detectors.py    # Unit test
├── requirements.txt
└── README.md
```

> Sesuaikan struktur di atas dengan struktur folder repo asli kamu.

---

## Roadmap

- [x] Engine deteksi berbasis CLI
- [x] Sistem risk scoring 0–100
- [x] Unit testing (16 test)
- [ ] Integrasi backend **FastAPI**
- [ ] Integrasi reputation API (VirusTotal, Google Safe Browsing)
- [ ] Dashboard web sederhana untuk hasil scan

---

## 👤 Kontak

**I Putu Willy Nugraha**
📧 wllygrh@gmail.com
🔗 [linkedin.com/in/willy-nugraha](https://linkedin.com/in/willy-nugraha)
