import mysql.connector
import tkinter as tk
from tkinter import messagebox

# CREATE TABLE IF NOT EXISTS Mahasiswa (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nama VARCHAR(255),
#     nim VARCHAR(255),
#     jurusan VARCHAR(255)
# );
# fungsi untuk membuat koneksi ke database
def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mahasiswa"
    )
    return conn

# fungsi untuk memasukkan data mahasiswa
def insert_mahasiswa(nama, nim, jurusan):
    def submit() :
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
    nama_label.grid(row=0, column=0, padx= 10, pady=10)
    nama_entry = tk.Entry(top)
    nama_entry.grid(row=0, column=1)
    
    nim_label = tk.Label(top, text="Nim")
    nim_label.grid(row=1, column=0, padx= 10, pady=10)
    nim_entry = tk.Entry(top)
    nim_entry.grid(row=1, column=1)
    
    jurusan_label = tk.Label(top, text="Jurusan")
    jurusan_label.grid(row=2, column=0, padx= 10, pady=10)
    jurusan_entry = tk.Entry(top)
    jurusan_entry.grid(row=2, column=1)

    submit_button = tk.Button(top, text="Simpan", command=submit)
    submit_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
# fungsi untuk menampilkan data mahasiswa
def show_mahasiswa():
    conn = connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM Mahasiswa"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data mahasiswa")
    else:
        for data in results:
            print(data)
    conn.close()

# fungsi untuk mengubah data mahasiswa
def update_mahasiswa(id, nama, nim, jurusan):
    conn = connect()
    cursor = conn.cursor()
    sql = "UPDATE Mahasiswa SET nama = %s, nim = %s, jurusan = %s WHERE id = %s"
    val = (nama, nim, jurusan, id)
    cursor.execute(sql, val)
    conn.commit()
    print("{} data mahasiswa berhasil diubah".format(cursor.rowcount))
    conn.close()

# fungsi untuk menghapus data mahasiswa
def delete_mahasiswa(id):
    conn = connect()
    cursor = conn.cursor()
    sql = "DELETE FROM Mahasiswa WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conn.commit()
    print("{} data mahasiswa berhasil dihapus".format(cursor.rowcount))
    conn.close()

# contoh penggunaan program
# insert_mahasiswa("John Doe", "123456", "Informatika")
# insert_mahasiswa("Jane Doe", "789012", "Teknik Elektro")
# show_mahasiswa()
# update_mahasiswa(1, "John Smith", "123456", "Teknik Mesin")
# delete_mahasiswa(2)
# show_mahasiswa()