import requests
from prettytable import PrettyTable
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SearchKota :
    def __init__(self, master):
        self.master = master
        self.master.title("Search Kota")
        self.create_widgets()

    def create_widgets(self):
        self.search_label = tk.Label(self.master, text="Search Kota", font=("Arial", 24))
        self.search_label.pack(pady=10)

        self.nama_kota_entry = tk.Entry(self.master, font=("Arial", 16))
        self.nama_kota_entry.pack(pady=5)

        self.search_button = tk.Button(self.master, text="Search", font=("Arial", 16), command=self.search_kota)
        self.search_button.pack(pady=5)

        self.hasil_label = tk.Label(self.master, text="", font=("Arial", 16))
        self.hasil_label.pack(pady=5)

    def search_kota(self):
        nama_kota = self.nama_kota_entry.get()
        api_url= f"https://api.myquran.com/v1/sholat/kota/cari/{nama_kota}"
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data= response.json()
                id = data['data']
                self.hasil_label.config(text=f"ID Kota: {id}")
            else:
                self.hasil_label.config(text="Kota tidak ditemukan")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "Tidak terkoneksi ke internet")


class JadwalSholatHarian:
    def __init__(self, master):
        self.master = master
        self.master.title("Jadwal Harian")
        self.create_widgets()
    
    def create_widgets(self) :
        kota_label = tk.Label(self.master, text="Kota:")
        kota_label.grid(row=0, column=0, padx=5, pady=5)

        self.kota_entry = tk.Entry(self.master, font=("Arial", 16))
        self.kota_entry.grid(row=0, column=1, padx=5, pady=5)

        tahun_label = tk.Label(self.master, text="Tahun:")
        tahun_label.grid(row=1, column=0, padx=5, pady=5)

        self.tahun_entry = tk.Entry(self.master, font=("Arial", 16))
        self.tahun_entry.grid(row=1, column=1, padx=5, pady=5)

        bulan_label = tk.Label(self.master, text="Bulan:")
        bulan_label.grid(row=2, column=0, padx=5, pady=5)

        self.bulan_entry = tk.Entry(self.master, font=("Arial", 16))
        self.bulan_entry.grid(row=2, column=1, padx=5, pady=5)

        tanggal_label = tk.Label(self.master, text="Tanggal:")
        tanggal_label.grid(row=3, column=0, padx=5, pady=5)

        self.tanggal_entry = tk.Entry(self.master, font=("Arial", 16))
        self.tanggal_entry.grid(row=3, column=1, padx=5, pady=5)

        jadwal_button = tk.Button(self.master, text="Tampilkan Jadwal Sholat", font=("Arial", 12), command=self.get_jadwal_harian)
        jadwal_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
        
    def get_jadwal_harian(self):
        kota = self.kota_entry.get()
        tahun = self.tahun_entry.get()
        bulan = self.bulan_entry.get()
        tanggal = self.tanggal_entry.get()
        api_url = f"https://api.myquran.com/v1/sholat/jadwal/{kota}/{tahun}/{bulan}/{tanggal}" 
        response = requests.get(api_url)
        try:
            data = response.json()
            jadwal_harian = data['data']['jadwal']
            if jadwal_harian is not None:
                # Menampilkan jadwal sholat harian pada messagebox
                messagebox.showinfo("Jadwal Sholat Harian", f"Shubuh      : {jadwal_harian['subuh']}\nDzuhur      : {jadwal_harian['dzuhur']}\nAshar       : {jadwal_harian['ashar']}\nMaghrib     : {jadwal_harian['maghrib']}\nIsya        : {jadwal_harian['isya']}")
            else:
                # Menampilkan pesan kesalahan pada messagebox jika terjadi error
                messagebox.showerror("Error", "Tidak dapat mengambil jadwal sholat harian, cek koneksi internet atau coba beberapa saat lagi.")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "Tidak terkoneksi ke internet")

class JadwalSholatBulanan():
    def __init__(self, master):
        self.master = master
        self.master.title("Jadwal Bulanan")
        self.create_widgets()
    
    def create_widgets(self):
        kota_label = tk.Label(self.master, text="Kota:")
        kota_label.grid(row=0, column=0, padx=5, pady=5)

        self.kota_entry = tk.Entry(self.master, font=("Arial", 16))
        self.kota_entry.grid(row=0, column=1, padx=5, pady=5)

        tahun_label = tk.Label(self.master, text="Tahun:")
        tahun_label.grid(row=1, column=0, padx=5, pady=5)

        self.tahun_entry = tk.Entry(self.master, font=("Arial", 16))
        self.tahun_entry.grid(row=1, column=1, padx=5, pady=5)

        bulan_label = tk.Label(self.master, text="Bulan:")
        bulan_label.grid(row=2, column=0, padx=5, pady=5)

        self.bulan_entry = tk.Entry(self.master, font=("Arial", 16))
        self.bulan_entry.grid(row=2, column=1, padx=5, pady=5)

        jadwal_button = tk.Button(self.master, text="Tampilkan Jadwal Sholat", font=("Arial", 12), command=self.get_jadwal_bulanan)
        jadwal_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
        
                # Membuat tabel untuk menampilkan jadwal sholat bulanan
        self.table = ttk.Treeview(self.master, columns=('Tanggal', 'Shubuh', 'Dzuhur', 'Ashar', 'Maghrib', 'Isya'), show='headings')
        self.table.heading('Tanggal', text='Tanggal')
        self.table.heading('Shubuh', text='Shubuh')
        self.table.heading('Dzuhur', text='Dzuhur')
        self.table.heading('Ashar', text='Ashar')
        self.table.heading('Maghrib', text='Maghrib')
        self.table.heading('Isya', text='Isya')
        self.table.grid(row = 4 ,column= 0, columnspan=4,padx=5, pady=10)
    def get_jadwal_bulanan(self):
        self.table.delete(*self.table.get_children()) # menghapus data lama pada tabel
        self.kota = self.kota_entry.get()
        self.tahun = self.tahun_entry.get()
        self.bulan = self.bulan_entry.get()
        api_url = f"https://api.myquran.com/v1/sholat/jadwal/{self.kota}/{self.tahun}/{self.bulan}"
        response = requests.get(api_url)
        try:
            data = response.json()
            response.raise_for_status() # menimbulkan exception jika kode status HTTP yang diterima adalah >= 400
            jadwal = data['data']['jadwal']
            # tabel = PrettyTable()
            # tabel.field_names =['Tanggal', 'Shubuh', 'Dzuhur', 'Ashar', 'Maghrib', 'Isya']
            if response.status_code == 200 :
                for jadwal in jadwal:
                    self.table.insert("", 'end', values=(jadwal['tanggal'], jadwal['subuh'], jadwal['dzuhur'], jadwal['ashar'], jadwal['maghrib'], jadwal['isya']))
                    
                    # # Buat scrollbar horizontal dan vertikal
                    # hscrollbar = ttk.Scrollbar(self.master, orient='horizontal', command=self.table.xview)
                    # hscrollbar.pack(side='bottom', fill='x')
                    # vscrollbar = ttk.Scrollbar(self.master, orient='vertical', command=self.table.yview)
                    # vscrollbar.pack(side='right', fill='y')

                    # # Pasangkan scrollbar dengan tabel
                    # self.table.configure(xscrollcommand=hscrollbar.set, yscrollcommand=vscrollbar.set)
            else:
                messagebox.showerror("Error", "Tidak dapat mengambil jadwal sholat harian, cek koneksi internet atau coba beberapa saat lagi.")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Error", "Tidak terkoneksi ke internet")
        
        
  
