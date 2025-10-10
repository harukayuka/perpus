import json
import os

DB_FILE = "user_db.json"

# --- load & save ---
def load_user():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def save_user(user_db):
    with open(DB_FILE, "w") as f:
        json.dump(user_db, f, indent=4)

# --- tambah user ---
def tambah_user():
    user_db = load_user()

    nis = input("Masukkan NIS: ")
    nama = input("Masukkan Nama: ")
    kelas = input("Masukkan Kelas: ")

    # cek kalau NIS sudah ada
    for u in user_db:
        if u["nis"] == nis:
            print("⚠️ User dengan NIS ini sudah ada.")
            return

    user = {
        "nis": nis,
        "nama": nama,
        "kelas": kelas
    }

    user_db.append(user)
    save_user(user_db)
    print("\n✅ User berhasil ditambahkan!\n")

# --- daftar user ---
def daftar_user():
    user_db = load_user()
    if not user_db:
        print("Belum ada user.")
        return
    for i, u in enumerate(user_db, start=1):
        print(f"{i}. {u['nis']} - {u['nama']} (Kelas {u['kelas']})")

# --- cari user ---
def cari_user(nis):
    user_db = load_user()
    for u in user_db:
        if u["nis"] == nis:
            return u
    return None

# --- contoh pemakaian ---
if __name__ == "__main__":
    while True:
        print("\n=== Menu User ===")
        print("1. Tambah User")
        print("2. Lihat Daftar User")
        print("3. Cari User")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_user()
        elif pilih == "2":
            daftar_user()
        elif pilih == "3":
            nis = input("Masukkan NIS: ")
            user = cari_user(nis)
            if user:
                print(f"✅ Ditemukan: {user['nama']} (Kelas {user['kelas']})")
            else:
                print("⚠️ User tidak ditemukan.")
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid!")
