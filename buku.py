import json
import os

DB_FILE = "buku_db.json"

STATUS_MAP = {
    1: "tersedia",
    2: "sedang dipinjam"
}

# --- load & save ---
def load_buku():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def save_buku(buku_db):
    with open(DB_FILE, "w") as f:
        json.dump(buku_db, f, indent=4)

# --- tambah buku ---
def tambah_buku():
    buku_db = load_buku()

    id_buku = input("Masukkan ID Buku: ")
    judul = input("Masukkan Judul Buku: ")
    penulis = input("Masukkan Penulis: ")
    penerbit = input("Masukkan Penerbit: ")
    tahun_terbit = input("Masukkan Tahun Terbit: ")
    tahun_masuk = input("Masukkan Tahun Masuk: ")
    sumber = input("Masukkan Sumber Buku: ")

    buku = {
        "id": id_buku,
        "judul": judul,
        "penulis": penulis,
        "penerbit": penerbit,
        "tahun_terbit": tahun_terbit,
        "tahun_masuk": tahun_masuk,
        "sumber": sumber,
        "status": 1   # default: tersedia
    }

    buku_db.append(buku)
    save_buku(buku_db)
    print("\n✅ Buku berhasil ditambahkan!\n")

# --- update status ---
def update_status_buku(id_buku, status_baru):
    buku_db = load_buku()
    for b in buku_db:
        if b["id"] == id_buku:
            if status_baru in STATUS_MAP:
                b["status"] = status_baru
                save_buku(buku_db)
                print(f"✅ Status buku {id_buku} diubah menjadi: {STATUS_MAP[status_baru]}")
                return
            else:
                print("⚠️ Status tidak valid (gunakan 1=tersedia, 2=sedang dipinjam)")
                return
    print(f"⚠️ Buku dengan ID {id_buku} tidak ditemukan.")

# --- daftar buku ---
def daftar_buku():
    buku_db = load_buku()
    if not buku_db:
        print("Belum ada buku.")
        return
    for i, b in enumerate(buku_db, start=1):
        status_text = STATUS_MAP.get(b["status"], "unknown")
        print(f"{i}. {b['id']} - {b['judul']} ({b['penulis']}) [{status_text}]")

# --- contoh pemakaian ---
if __name__ == "__main__":
    while True:
        print("\n=== Menu Buku ===")
        print("1. Tambah Buku")
        print("2. Lihat Daftar Buku")
        print("3. Update Status Buku")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_buku()
        elif pilih == "2":
            daftar_buku()
        elif pilih == "3":
            id_buku = input("Masukkan ID Buku: ")
            try:
                status = int(input("Masukkan status baru (1=tersedia, 2=sedang dipinjam): "))
            except ValueError:
                print("⚠️ Status harus angka 1 atau 2")
                continue
            update_status_buku(id_buku, status)
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid!")
