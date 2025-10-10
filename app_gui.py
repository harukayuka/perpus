import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import buku
import database_user
import peminjam

class PerpustakaanApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Perpustakaan")
        self.geometry("600x500")
        self.create_main_menu()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_main_menu(self):
        self.clear_frame()
        tk.Label(self, text="SISTEM PERPUSTAKAAN", font=("Arial", 18)).pack(pady=20)
        tk.Button(self, text="Kelola Buku", width=30, command=self.menu_buku).pack(pady=10)
        tk.Button(self, text="Kelola User", width=30, command=self.menu_user).pack(pady=10)
        tk.Button(self, text="Kelola Peminjaman", width=30, command=self.menu_peminjam).pack(pady=10)
        tk.Button(self, text="Keluar", width=30, command=self.quit).pack(pady=10)

    # --- Menu Buku ---
    def menu_buku(self):
        self.clear_frame()
        tk.Label(self, text="Menu Buku", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Tambah Buku", width=25, command=self.tambah_buku).pack(pady=5)
        tk.Button(self, text="Lihat Daftar Buku", width=25, command=self.daftar_buku).pack(pady=5)
        tk.Button(self, text="Update Status Buku", width=25, command=self.update_status_buku).pack(pady=5)
        tk.Button(self, text="Kembali", width=25, command=self.create_main_menu).pack(pady=5)

    def tambah_buku(self):
        fields = ["ID Buku", "Judul", "Penulis", "Penerbit", "Tahun Terbit", "Tahun Masuk", "Sumber"]
        values = []
        for f in fields:
            val = simpledialog.askstring("Tambah Buku", f)
            if val is None:
                return
            values.append(val)
        buku_db = buku.load_buku()
        buku_baru = {
            "id": values[0], "judul": values[1], "penulis": values[2], "penerbit": values[3],
            "tahun_terbit": values[4], "tahun_masuk": values[5], "sumber": values[6], "status": 1
        }
        buku_db.append(buku_baru)
        buku.save_buku(buku_db)
        messagebox.showinfo("Info", "Buku berhasil ditambahkan!")

    def daftar_buku(self):
        buku_db = buku.load_buku()
        win = tk.Toplevel(self)
        win.title("Daftar Buku")
        txt = scrolledtext.ScrolledText(win, width=70, height=20)
        txt.pack()
        if not buku_db:
            txt.insert(tk.END, "Belum ada buku.")
        else:
            for b in buku_db:
                status = buku.STATUS_MAP.get(b["status"], "unknown")
                txt.insert(tk.END, f"{b['id']} - {b['judul']} ({b['penulis']}) [{status}]\n")

    def update_status_buku(self):
        id_buku = simpledialog.askstring("Update Status", "Masukkan ID Buku:")
        if id_buku is None:
            return
        status = simpledialog.askinteger("Update Status", "Masukkan status baru (1=tersedia, 2=sedang dipinjam):")
        if status is None:
            return
        msg = buku.update_status_buku(id_buku, status)
        messagebox.showinfo("Info", msg if msg else "Status buku diupdate.")

    # --- Menu User ---
    def menu_user(self):
        self.clear_frame()
        tk.Label(self, text="Menu User", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Tambah User", width=25, command=self.tambah_user).pack(pady=5)
        tk.Button(self, text="Lihat Daftar User", width=25, command=self.daftar_user).pack(pady=5)
        tk.Button(self, text="Cari User", width=25, command=self.cari_user).pack(pady=5)
        tk.Button(self, text="Kembali", width=25, command=self.create_main_menu).pack(pady=5)

    def tambah_user(self):
        nis = simpledialog.askstring("Tambah User", "Masukkan NIS:")
        if nis is None:
            return
        nama = simpledialog.askstring("Tambah User", "Masukkan Nama:")
        if nama is None:
            return
        kelas = simpledialog.askstring("Tambah User", "Masukkan Kelas:")
        if kelas is None:
            return
        user_db = database_user.load_user()
        for u in user_db:
            if u["nis"] == nis:
                messagebox.showwarning("Peringatan", "User dengan NIS ini sudah ada.")
                return
        user = {"nis": nis, "nama": nama, "kelas": kelas}
        user_db.append(user)
        database_user.save_user(user_db)
        messagebox.showinfo("Info", "User berhasil ditambahkan!")

    def daftar_user(self):
        user_db = database_user.load_user()
        win = tk.Toplevel(self)
        win.title("Daftar User")
        txt = scrolledtext.ScrolledText(win, width=70, height=20)
        txt.pack()
        if not user_db:
            txt.insert(tk.END, "Belum ada user.")
        else:
            for u in user_db:
                txt.insert(tk.END, f"{u['nis']} - {u['nama']} (Kelas {u['kelas']})\n")

    def cari_user(self):
        nis = simpledialog.askstring("Cari User", "Masukkan NIS:")
        if nis is None:
            return
        user = database_user.cari_user(nis)
        if user:
            messagebox.showinfo("Info", f"Ditemukan: {user['nama']} (Kelas {user['kelas']})")
        else:
            messagebox.showwarning("Peringatan", "User tidak ditemukan.")

    # --- Menu Peminjam ---
    def menu_peminjam(self):
        self.clear_frame()
        tk.Label(self, text="Menu Peminjam", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Tambah Peminjam", width=25, command=self.tambah_peminjam).pack(pady=5)
        tk.Button(self, text="Lihat Daftar Peminjam", width=25, command=self.daftar_peminjam).pack(pady=5)
        tk.Button(self, text="Kembalikan Buku", width=25, command=self.kembalikan_buku).pack(pady=5)
        tk.Button(self, text="Kembali", width=25, command=self.create_main_menu).pack(pady=5)

    def tambah_peminjam(self):
        nis = simpledialog.askstring("Tambah Peminjam", "Masukkan NIS peminjam:")
        if nis is None:
            return
        id_buku = simpledialog.askstring("Tambah Peminjam", "Masukkan ID Buku yang dipinjam:")
        if id_buku is None:
            return
        tanggal_pinjam = simpledialog.askstring("Tambah Peminjam", "Masukkan tanggal pinjam (YYYY-MM-DD):")
        if tanggal_pinjam is None:
            return
        tanggal_kembali = simpledialog.askstring("Tambah Peminjam", "Masukkan tanggal kembali (YYYY-MM-DD):")
        if tanggal_kembali is None:
            return
        msg = peminjam.tambah_peminjam_gui(nis, id_buku, tanggal_pinjam, tanggal_kembali)
        messagebox.showinfo("Info", msg)

    def daftar_peminjam(self):
        peminjam_db = peminjam.load_peminjam()
        win = tk.Toplevel(self)
        win.title("Daftar Peminjam")
        txt = scrolledtext.ScrolledText(win, width=70, height=20)
        txt.pack()
        if not peminjam_db:
            txt.insert(tk.END, "Belum ada data peminjam.")
        else:
            for p in peminjam_db:
                txt.insert(tk.END, f"{p['nis']} - {p['nama']} | Buku: {p['judul']} | Pinjam: {p['tanggal_pinjam']} - Kembali: {p['tanggal_kembali']}\n")

    def kembalikan_buku(self):
        id_buku = simpledialog.askstring("Kembalikan Buku", "Masukkan ID Buku yang dikembalikan:")
        if id_buku is None:
            return
        msg = peminjam.kembalikan_buku_gui(id_buku)
        messagebox.showinfo("Info", msg)

if __name__ == "__main__":
    # Tambahkan fungsi GUI ke peminjam.py
    if not hasattr(peminjam, "tambah_peminjam_gui"):
        def tambah_peminjam_gui(nis, id_buku, tanggal_pinjam, tanggal_kembali):
            peminjam_db = peminjam.load_peminjam()
            user_db = database_user.load_user()
            buku_db = buku.load_buku()
            user = next((u for u in user_db if u["nis"] == nis), None)
            if not user:
                return "User tidak ditemukan."
            buku_item = next((b for b in buku_db if b["id"] == id_buku), None)
            if not buku_item:
                return "Buku tidak ditemukan."
            if buku_item["status"] != 1:
                return "Buku sedang dipinjam."
            peminjaman = {
                "nis": nis,
                "nama": user["nama"],
                "id_buku": id_buku,
                "judul": buku_item["judul"],
                "tanggal_pinjam": tanggal_pinjam,
                "tanggal_kembali": tanggal_kembali
            }
            peminjam_db.append(peminjaman)
            peminjam.save_peminjam(peminjam_db)
            buku_item["status"] = 2
            buku.save_buku(buku_db)
            return "Data peminjaman berhasil ditambahkan!"
        peminjam.tambah_peminjam_gui = tambah_peminjam_gui
    if not hasattr(peminjam, "kembalikan_buku_gui"):
        def kembalikan_buku_gui(id_buku):
            peminjam_db = peminjam.load_peminjam()
            buku_db = buku.load_buku()
            peminjaman = next((p for p in peminjam_db if p["id_buku"] == id_buku), None)
            if not peminjaman:
                return "Data peminjaman tidak ditemukan."
            buku_item = next((b for b in buku_db if b["id"] == id_buku), None)
            if buku_item:
                buku_item["status"] = 1
                buku.save_buku(buku_db)
            peminjam_db = [p for p in peminjam_db if p["id_buku"] != id_buku]
            peminjam.save_peminjam(peminjam_db)
            return "Buku berhasil dikembalikan!"
        peminjam.kembalikan_buku_gui = kembalikan_buku_gui
    app = PerpustakaanApp()
    app.mainloop()
