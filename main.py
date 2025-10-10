
import buku
import database_user
import peminjam
import password

if __name__ == "__main__":
    print("=== SISTEM PERPUSTAKAAN ===")
    # Cek password sebelum masuk ke menu utama
    if not password.check_password():
        exit()
    while True:
        print("\n=== SISTEM PERPUSTAKAAN ===")
        print("1. Kelola Buku")
        print("2. Kelola User")
        print("3. Kelola Peminjaman")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            # menu buku
            while True:
                print("\n=== Menu Buku ===")
                print("1. Tambah Buku")
                print("2. Lihat Daftar Buku")
                print("3. Update Status Buku")
                print("4. Kembali ke Menu Utama")
                sub = input("Pilih: ")
                if sub == "1":
                    buku.tambah_buku()
                elif sub == "2":
                    buku.daftar_buku()
                elif sub == "3":
                    id_buku = input("Masukkan ID Buku: ")
                    try:
                        status = int(input("Masukkan status baru (1=tersedia, 2=sedang dipinjam): "))
                    except ValueError:
                        print("⚠️ Status harus angka 1 atau 2")
                        continue
                    buku.update_status_buku(id_buku, status)
                elif sub == "4":
                    break
                else:
                    print("Pilihan tidak valid!")
        elif pilih == "2":
            # menu user
            while True:
                print("\n=== Menu User ===")
                print("1. Tambah User")
                print("2. Lihat Daftar User")
                print("3. Cari User")
                print("4. Kembali ke Menu Utama")
                sub = input("Pilih: ")
                if sub == "1":
                    database_user.tambah_user()
                elif sub == "2":
                    database_user.daftar_user()
                elif sub == "3":
                    nis = input("Masukkan NIS: ")
                    user = database_user.cari_user(nis)
                    if user:
                        print(f"✅ Ditemukan: {user['nama']} (Kelas {user['kelas']})")
                    else:
                        print("⚠️ User tidak ditemukan.")
                elif sub == "4":
                    break
                else:
                    print("Pilihan tidak valid!")
        elif pilih == "3":
            # menu peminjam
            while True:
                print("\n=== Menu Peminjam ===")
                print("1. Tambah Peminjam")
                print("2. Lihat Daftar Peminjam")
                print("3. Kembalikan Buku")
                print("4. Kembali ke Menu Utama")
                sub = input("Pilih: ")
                if sub == "1":
                    peminjam.tambah_peminjam()
                elif sub == "2":
                    peminjam.daftar_peminjam()
                elif sub == "3":
                    peminjam.kembalikan_buku()
                elif sub == "4":
                    break
                else:
                    print("Pilihan tidak valid!")
        elif pilih == "4":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid!")
