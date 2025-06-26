# Kontrol Mouse dengan Pelacakan Wajah dan Klik Senyum

Aplikasi Python yang menggunakan computer vision untuk mengontrol kursor mouse dengan gerakan kepala dan memicu klik dengan tersenyum. Proyek ini menggunakan OpenCV untuk deteksi wajah dan PyAutoGUI untuk kontrol mouse.

## Fitur

- **Pelacakan Kepala**: Gerakkan kursor mouse dengan menggerakkan kepala
- **Deteksi Senyum**: Klik dengan tersenyum ke kamera
- **Gerakan Halus**: Mengimplementasikan algoritma smoothing untuk gerakan kursor yang natural
- **Jeda Klik**: Mencegah klik ganda yang tidak disengaja
- **Umpan Balik Visual Real-time**: Menampilkan kotak deteksi wajah dan senyum

## Persyaratan

- Python 3.7 atau lebih tinggi
- Webcam/Kamera
- Windows, macOS, atau Linux

## Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/DandiKurnia/Kelompok-4-Kontrol-Mouse-Menggunakan-Gerakan-Kepala
cd Kelompok-4-Kontrol-Mouse-Menggunakan-Gerakan-Kepala
```

### 2. Install Library yang Diperlukan

```bash
pip install opencv-python
pip install numpy
pip install pyautogui
```

Atau install semua dependencies sekaligus:

```bash
pip install opencv-python numpy pyautogui
```

## Cara Penggunaan

### Menjalankan Aplikasi

```bash
python mouse_head2.py.py
```

### Kontrol

- **Gerakan Mouse**: Gerakkan kepala untuk mengontrol kursor
- **Klik**: Tersenyum untuk memicu klik mouse
- **Keluar**: Tekan tombol `ESC` untuk keluar dari aplikasi

### Konfigurasi

Anda dapat menyesuaikan parameter berikut dalam kode:

```python
# Faktor smoothing (0.1 = lebih halus, 0.9 = lebih responsif)
alpha = 0.2

# Jeda klik dalam detik
click_cooldown = 1.5

# Sensitivitas deteksi senyum
scaleFactor = 1.7      # Lebih rendah = lebih sensitif
minNeighbors = 22      # Lebih rendah = lebih sensitif
minSize = (25, 25)     # Ukuran minimum senyum
```

## Cara Kerja

1. **Deteksi Wajah**: Menggunakan Haar Cascade classifier untuk mendeteksi wajah secara real-time
2. **Pelacakan Kepala**: Menghitung pusat wajah dan memetakannya ke koordinat layar
3. **Smoothing**: Menerapkan exponential smoothing untuk gerakan kursor yang natural
4. **Deteksi Senyum**: Mendeteksi senyum dalam area wajah
5. **Kontrol Klik**: Memicu klik mouse saat senyum terdeteksi dengan perlindungan cooldown

## Pemecahan Masalah

### Masalah Umum

**Kamera tidak berfungsi:**

```python
# Coba indeks kamera yang berbeda
cap = cv2.VideoCapture(1)  # atau 2, 3, dst.
```

**Error permission (macOS):**

- Buka System Preferences > Security & Privacy > Privacy > Camera
- Izinkan Terminal atau IDE Anda untuk mengakses kamera

**Fitur keamanan PyAutoGUI:**

```python
# Nonaktifkan fail-safe (gerakkan mouse ke sudut untuk berhenti)
pyautogui.FAILSAFE = False

# Sesuaikan jeda antar aksi
pyautogui.PAUSE = 0.1
```

**Akurasi deteksi buruk:**

- Pastikan kondisi pencahayaan yang baik
- Posisikan wajah dengan jelas di depan kamera
- Sesuaikan parameter deteksi untuk lingkungan Anda

## Struktur Proyek

```
kontrol-mouse-pelacakan-wajah/
│
├── face_mouse_control.py    # File aplikasi utama
├── README.md               # File ini
```

## Detail Teknis

### Library yang Digunakan

- **OpenCV (cv2)**: Library computer vision untuk deteksi wajah dan senyum
- **NumPy**: Operasi numerik dan penanganan array
- **PyAutoGUI**: Otomasi mouse dan keyboard lintas platform

### Haar Cascades

Proyek ini menggunakan Haar Cascade classifier yang sudah dilatih:

- `haarcascade_frontalface_default.xml`: Untuk deteksi wajah
- `haarcascade_smile.xml`: Untuk deteksi senyum

## Kontribusi

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/fitur-baru`)
3. Commit perubahan Anda (`git commit -am 'Tambah fitur baru'`)
4. Push ke branch (`git push origin feature/fitur-baru`)
5. Buat Pull Request

## Penghargaan

- Komunitas OpenCV untuk tools computer vision
- Haar Cascade classifiers dari OpenCV
- PyAutoGUI untuk otomasi lintas platform

## Pengembangan Masa Depan

- [ ] Deteksi kedipan mata untuk kontrol tambahan
- [ ] Pengenalan gesture untuk klik kanan
- [ ] Sistem kalibrasi untuk pengguna berbeda
- [ ] Panel konfigurasi GUI
- [ ] Dukungan pelacakan multi-wajah
