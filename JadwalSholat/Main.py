from JadwalSholat import *

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App:
    def __init__ (self, master):
        self.master = master
        self.master.title("Jadwal Sholat")
        self.label_title = ttk.Label(master, text ="Selamat Datang Di Aplikasi Pencarian Jadwal Sholat", font=('Helvetica', 16, 'bold'))
        self.label_menu = ttk.Label(master, text = "Menu", font=('Helvetica', 14, 'bold'))
        self.button_search_kota = ttk.Button(master, text="1. Search Kota", command=self.on_button_search_kota)
        self.button_jadwal_harian = ttk.Button(master, text="2. Jadwal Harian", command=self.on_button_jadwal_harian)
        self.button_jadwal_bulanan = ttk.Button(master, text="3. Jadwal Bulanan", command=self.on_button_jadwal_bulanan)
        self.button_exit = ttk.Button(master, text="4. Exit", command=self.on_button_exit)
        
        # Grid Layout
        self.label_title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.label_menu.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        self.button_search_kota.grid(row=2, column=0, padx=10, pady=10)
        self.button_jadwal_harian.grid(row=2, column=1, padx=10, pady=10)
        self.button_jadwal_bulanan.grid(row=2, column=2, padx=10, pady=10)
        self.button_exit.grid(row=2, column=3, padx=10, pady=10)
        
        
    def on_button_search_kota(self):
        search_window = tk.Toplevel(self.master)
        app = SearchKota(search_window)
        
    def on_button_jadwal_harian(self):
        jadwal_harian_window = tk.Toplevel(self.master)
        harian = JadwalSholatHarian(jadwal_harian_window)
        
    def on_button_jadwal_bulanan(self):
        jadwal_bulanan_window = tk.Toplevel(self.master)
        bulanan = JadwalSholatBulanan(jadwal_bulanan_window)
    def on_button_exit(self):
        if messagebox.askyesno("Konfirmasi", "Anda yakin ingin keluar?"):
            self.master.destroy()
            messagebox.showinfo("Exit", "Terimakasih Telah Berkunjung")
    
root = tk.Tk()
jadwal_sholat_app = App(root)
root.mainloop()