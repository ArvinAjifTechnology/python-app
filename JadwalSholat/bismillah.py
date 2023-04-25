import tkinter as tk
import requests

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Menu")
        self.create_widgets()

    def create_widgets(self):
        self.menu_label = tk.Label(self.master, text="Main Menu", font=("Arial", 24))
        self.menu_label.pack(pady=10)

        self.menu_button1 = tk.Button(self.master, text="Menu 1", font=("Arial", 16), command=self.menu1)
        self.menu_button1.pack(pady=5)

        self.menu_button2 = tk.Button(self.master, text="Menu 2", font=("Arial", 16), command=self.menu2)
        self.menu_button2.pack(pady=5)

    def menu1(self):
        # code to display menu 1
        pass

    def menu2(self):
        search_window = tk.Toplevel(self.master)
        app = SearchKota(search_window)

class SearchKota:
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
        response = requests.get(api_url)
        if response.status_code == 200:
            data= response.json()
            id = data['data']
            self.hasil_label.config(text=f"ID Kota: {id}")
        else:
            self.hasil_label.config(text="Kota tidak ditemukan")

root = tk.Tk()
app = MainMenu(root)
root.mainloop()


# kota_label = tk.Label(self.master, text="Kota:")
#         kota_label.grid(row=0, column=0, padx=5, pady=5)

#         kota_entry = tk.Entry(self.master, font=("Arial", 16))
#         kota_entry.grid(row=0, column=1, padx=5, pady=5)

#         tahun_label = tk.Label(self.master, text="Tahun:")
#         tahun_label.grid(row=1, column=0, padx=5, pady=5)

#         tahun_entry = tk.Entry(self.master, font=("Arial", 16))
#         tahun_entry.grid(row=1, column=1, padx=5, pady=5)

#         bulan_label = tk.Label(self.master, text="Bulan:")
#         bulan_label.grid(row=2, column=0, padx=5, pady=5)

#         bulan_entry = tk.Entry(self.master, font=("Arial", 16))
#         bulan_entry.grid(row=2, column=1, padx=5, pady=5)

#         tanggal_label = tk.Label(self.master, text="Tanggal:")
#         tanggal_label.grid(row=3, column=0, padx=5, pady=5)

#         tanggal_entry = tk.Entry(self.master, font=("Arial", 16))
#         tanggal_entry.grid(row=3, column=1, padx=5, pady=5)

#         jadwal_button = tk.Button(self.master, text="Tampilkan Jadwal Sholat", font=("Arial", 12), command= self.get_jadwal_harian)
#         jadwal_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)



        
        # # Create Widgets
        # self.label_kota = ttk.Label(master, text ="Kota")
        # self.entry_kota = ttk.Entry(master)
        # self.label_tanggal = ttk.Label(master, text = "Tanggal (dd/mm/yyyy)")
        # self.entry_tanggal = ttk.Entry(master)
        # self.button_cari = ttk.Button(master, text="Cari", command=self.on_button_cari)
        # self.treeview_jadwal = ttk.Treeview(master, columns=("shubuh", "dzuhur", "ashar", "maghrib", "isya"))