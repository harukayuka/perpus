import buku
import database_user
import peminjam

if __name__ == "__main__":
    while True:
        print("\n=== SISTEM PERPUSTAKAAN ===")
        print("1. Kelola Buku")
        print("2. Kelola User")
        print("3. Kelola Peminjaman")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            # menu buku
            buku.menu_buku()
        elif pilih == "2":
            # menu user
            database_user.menu_user()
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
                    print("Pilihan salah!")
        elif pilih == "4":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid!")
