import getpass
import hashlib
import os

PASSWORD_FILE = "password_db.txt"

def set_password():
    password = getpass.getpass("Buat password baru: ")
    confirm = getpass.getpass("Konfirmasi password: ")
    if password != confirm:
        print("Password tidak cocok!")
        return False
    hashed = hashlib.sha256(password.encode()).hexdigest()
    with open(PASSWORD_FILE, "w") as f:
        f.write(hashed)
    print("Password berhasil disimpan.")
    return True

def check_password():
    if not os.path.exists(PASSWORD_FILE):
        print("Belum ada password. Silakan buat password dulu.")
        return set_password()
    password = getpass.getpass("Masukkan password: ")
    with open(PASSWORD_FILE, "r") as f:
        saved = f.read().strip()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if hashed == saved:
        return True
    else:
        print("Password salah!")
        return False

if __name__ == "__main__":
    print("=== Pengaturan Password Sistem ===")
    while True:
        print("1. Set Password Baru")
        print("2. Cek Password")
        print("3. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            set_password()
        elif pilih == "2":
            if check_password():
                print("Password benar!")
        elif pilih == "3":
            break
        else:
            print("Pilihan tidak valid!")
