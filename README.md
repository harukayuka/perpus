# Perpus (Sistem Perpustakaan)

**Perpus** adalah aplikasi manajemen perpustakaan sederhana berbasis Python, yang memungkinkan pengelolaan buku, peminjaman, pengembalian, dan data peminjam.

## 🎯 Fitur Utama

- CRUD (Create, Read, Update, Delete) data buku  
- CRUD data peminjam  
- Peminjaman buku  
- Pengembalian buku  
- Pencetakan laporan / ringkasan (opsional, tergantung implementasi)  
- Validasi input agar data tetap konsisten  

## 📁 Struktur Proyek

perpus/
├── buku.py
├── main.py
├── peminjam.py
└── README.md

Keterangan file:

- `main.py` — titik masuk aplikasi, navigasi menu  
- `buku.py` — modul terkait operasi buku  
- `peminjam.py` — modul terkait operasi peminjam  
- `README.md` — dokumentasi proyek (ini file-nya)  
