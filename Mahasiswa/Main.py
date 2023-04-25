from Mahasiswa import *

import tkinter as tk
from tkinter import ttk, messagebox

class App:
    def __init__ (self, master):
        self.master = master
        self.master.title("Jadwal Sholat")
        self.label_title = ttk.Label(master, text ="Selamat Datang Di Aplikasi Tambah Data Mahasiswa", font=('Helvetica', 16, 'bold'))
        self.label_menu = ttk.Label(master, text = "Menu", font=('Helvetica', 14, 'bold'))
        self.button_insert_mahasiswa = ttk.Button(master, text="1. Tambah Data Mahasiswa", command=self.on_button_insert_mahasiswa)
        self.button_show_mahasiswa = ttk.Button(master, text="2. Show Mahasiswa", command=self.on_button_show_mahasiswa)
        self.button_update_mahasiswa = ttk.Button(master, text="3. Update Mahasiswa", command=self.on_button_update_mahasiswa)
        self.button_delete_mahasiswa = ttk.Button(master, text="3. Update Mahasiswa", command=self.on_button_delete_mahasiswa)
        self.button_exit = ttk.Button(master, text="4. Exit", command=self.on_button_exit)
        
        # Grid Layout
        self.label_title.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.label_menu.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        self.button_insert_mahasiswa.grid(row=2, column=0, padx=10, pady=10)
        self.button_show_mahasiswa.grid(row=2, column=1, padx=10, pady=10)
        self.button_update_mahasiswa.grid(row=2, column=2, padx=10, pady=10)
        self.button_delete_mahasiswa.grid(row=2, column=3, padx=10, pady=10)
        self.button_exit.grid(row=2, column=4, padx=10, pady=10)
        
        
    def on_button_insert_mahasiswa(self):
        insert_mahasiswa(None, None, None)
        
    def on_button_show_mahasiswa(self):
        show_mahasiswa()
        
    def on_button_update_mahasiswa(self):
        update_mahasiswa(None, None, None, None)
    
    def on_button_delete_mahasiswa(self):
        delete_mahasiswa(None)

    def on_button_exit(self):
        if messagebox.askyesno("Konfirmasi", "Anda yakin ingin keluar?"):
            self.master.destroy()
            messagebox.showinfo("Exit", "Terimakasih Telah Berkunjung")
    
root = tk.Tk()
jadwal_sholat_app = App(root)
root.mainloop()