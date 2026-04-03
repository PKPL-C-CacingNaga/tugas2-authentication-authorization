# Panduan Menjalankan Aplikasi Secara Lokal

### 1. Clone Repositori
```bash
git clone <URL_REPOSITORI>
cd tugas2-authentication-authorization
```

### 2. Membuat dan Mengaktifkan Virtual Environment
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalasi Dependencies
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Environment Variables (.env)
Buat file bernama .env di direktori utama proyek (sejajar dengan manage.py) dan isi dengan kredensial berikut:
```env
GOOGLE_CLIENT_ID="isi_client_id_anda"
GOOGLE_CLIENT_SECRET="isi_client_secret_anda"
```

### 5. Persiapan Database
```bash
python manage.py migrate
```

### 6. Menjalankan Server
```bash
python manage.py runserver
```

Aplikasi dapat diakses melalui browser di: http://localhost:8000/
