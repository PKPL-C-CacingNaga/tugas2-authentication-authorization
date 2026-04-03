# Panduan Menjalankan Aplikasi Secara Lokal

### 1. Clone Repositori
Extract file ZIP ke folder lokal, lalu buka "Tugas2_source_CacingNaga".

### 2. Membuat dan Mengaktifkan Virtual Environment
Windows:
```bash
python -m venv env
env\Scripts\activate
```
macOS/Linux:
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Instalasi Dependencies
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Environment Variables (.env)
File .env sudah disertakan dalam folder, jadi tidak perlu membuat file .env baru.

### 5. Persiapan Database
```bash
python manage.py migrate
```

### 6. Menjalankan Server
```bash
python manage.py runserver
```

Aplikasi dapat diakses melalui browser di: http://localhost:8000/