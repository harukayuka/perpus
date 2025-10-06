import json
import os
from buku import load_buku, save_buku, STATUS_MAP
from database_user import load_user

DB_FILE = "peminjam_db.json"

def load_peminjam():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def save_peminjam(peminjam_db):
    with open(DB_FILE, "w") as f:
        json.dump(peminjam_db, f, indent=4)

def tambah_peminjam():
    peminjam_db = load_peminjam()
    user_db = load_user()
    buku_db = load_buku()

    nis = input("Masukkan NIS peminjam: ")
    user = next((u for u in user_db if u["nis"] == nis), None)
    if not user:
        print("⚠️ User tidak ditemukan.")
        return

    id_buku = input("Masukkan ID Buku yang dipinjam: ")
    buku = next((b for b in buku_db if b["id"] == id_buku), None)
    if not buku:
        print("⚠️ Buku tidak ditemukan.")
        return
    if buku["status"] != 1:
        print("⚠️ Buku sedang dipinjam.")
        return

    tanggal_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")
    tanggal_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")

    peminjaman = {
        "nis": nis,
        "nama": user["nama"],
        "id_buku": id_buku,
        "judul": buku["judul"],
        "tanggal_pinjam": tanggal_pinjam,
        "tanggal_kembali": tanggal_kembali
    }

    peminjam_db.append(peminjaman)
    save_peminjam(peminjam_db)

    # update status buku
    buku["status"] = 2
    save_buku(buku_db)

    print("\n✅ Data peminjaman berhasil ditambahkan!\n")

def daftar_peminjam():
    peminjam_db = load_peminjam()
    if not peminjam_db:
        print("Belum ada data peminjam.")
        return
    for i, p in enumerate(peminjam_db, start=1):
        print(f"{i}. {p['nis']} - {p['nama']} | Buku: {p['judul']} | Pinjam: {p['tanggal_pinjam']} - Kembali: {p['tanggal_kembali']}")

def kembalikan_buku():
    peminjam_db = load_peminjam()
    buku_db = load_buku()
    id_buku = input("Masukkan ID Buku yang dikembalikan: ")

    peminjaman = next((p for p in peminjam_db if p["id_buku"] == id_buku), None)
    if not peminjaman:
        print("⚠️ Data peminjaman tidak ditemukan.")
        return

    # update status buku
    buku = next((b for b in buku_db if b["id"] == id_buku), None)
    if buku:
        buku["status"] = 1
        save_buku(buku_db)

    # hapus data peminjaman
    peminjam_db = [p for p in peminjam_db if p["id_buku"] != id_buku]
    save_peminjam(peminjam_db)

    print("\n✅ Buku berhasil dikembalikan!\n")

if __name__ == "__main__":
    while True:
        print("\n=== Menu Peminjam ===")
        print("1. Tambah Peminjam")
        print("2. Lihat Daftar Peminjam")
        print("3. Kembalikan Buku")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_peminjam()
        elif pilih == "2":
            daftar_peminjam()
        elif pilih == "3":
            kembalikan_buku()
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid!")