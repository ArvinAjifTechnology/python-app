import mysql.connector
import tkinter as tk
from tkinter import messagebox

def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mahasiswa"
    )
    return conn

def insert_mahasiswa():
    def submit():
        nama = nama_entry.get()
        nim = nim_entry.get()
        jurusan = jurusan_entry.get()
        if nama == "" or nim == "" or jurusan == "":
            messagebox.showerror("Error", "Silakan isi semua kolom")
        else:
            conn = connect()
            cursor = conn.cursor()
            sql = "INSERT INTO Mahasiswa (nama, nim, jurusan) VALUES (%s, %s, %s)"
            val = (nama, nim, jurusan)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("Sukses", "Data mahasiswa berhasil disimpan")
            conn.close()
            top.destroy()

    top = tk.Toplevel()
    top.title("Tambah Data Mahasiswa")

    nama_label = tk.Label(top, text="Nama")
    nama_label.grid(row=0, column=0, padx=10, pady=10)
    nama_entry = tk.Entry(top)
    nama_entry.grid(row=0, column=1)

    nim_label = tk.Label(top, text="NIM")
    nim_label.grid(row=1, column=0, padx=10, pady=10)
    nim_entry = tk.Entry(top)
    nim_entry.grid(row=1, column=1)

    jurusan_label = tk.Label(top, text="Jurusan")
    jurusan_label.grid(row=2, column=0, padx=10, pady=10)
    jurusan_entry = tk.Entry(top)
    jurusan_entry.grid(row=2, column=1)

    submit_button = tk.Button(top, text="Simpan", command=submit)
    submit_button.grid(row=3, column=1, pady=10)

def show_mahasiswa():
    conn = connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM Mahasiswa"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data mahasiswa")
    else:
        top = tk.Toplevel()
        top.title("Data Mahasiswa")

        scrollbar = tk.Scrollbar(top)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(top, yscrollcommand=scrollbar.set)
        for data in results:
            listbox.insert(tk.END, data)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        scrollbar.config(command=listbox.yview)

    conn.close()

def update_mahasiswa():
    def submit():
        id = id_entry.get()
        nama = nama_entry.get()
        nim = nim_entry.get()
        jurusan = jurusan_entry.get()
        if id == "" or nama == "" or nim == "" or jurusan == "":
            messagebox.showerror("Error", "Silakan isi semua kolom")
        else:
            conn = connect()
            cursor = conn.cursor()
            sql = "UPDATE Mahasiswa SET nama = %s, nim = %s, jurusan = %s WHERE id = %s"
            val = (nama, nim, jurusan, id)
            cursor.execute(sql, val)
            conn.commit()
            messagebox.showinfo("Sukses", "Data mahasiswa berhasil diubah")
           
