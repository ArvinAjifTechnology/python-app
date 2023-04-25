# import pandas as pd

# def f(x):
#     x_soal = x
#     print(x_soal)
#     return x_soal
# def bisection(x1, x2, tol):
#     iterasi = 0
#     print("Metode Bisection")
#     print("Langkah 1: Tentukan tebakan awal x1 dan x2, serta toleransi error tol")
#     print("x1 = {:.6f}, x2 = {:.6f}, tol = {:.6f}".format(x1, x2, tol))
#     print("Langkah 2: Hitung f(x1) dan f(x2)")
#     fa = f(x1)
#     fb = f(x2)
#     print("f(x1) = {:.6f}, f(x2) = {:.6f}".format(fa, fb))
#     df = pd.DataFrame(columns=['Iterasi', 'x1', 'x2', 'xt', 'f(x1)','f(x2)', 'f(xt)'])
#     df.loc[iterasi] = [iterasi, x1, x2, None, fa, fb ,None]
#     print("Iterasi {}: x1 = {:.6f}, x2 = {:.6f}, f(x1) = {:.6f}, f(x2) = {:.6f}".format(iterasi, x1, x2, fa, fb))
#     while abs(x2 - x1) > tol:
#         iterasi += 1
#         print(f"Langkah 3: Hitung iterasi ke {iterasi}")
#         xt = (x1 + x2) / 2
#         print("xt = ({:.6f} + {:.6f}) / 2".format(x1,x2))
#         print("xt = {:.6f}".format(xt))
#         print("Langkah 4: Hitung f(xt)")
#         fc = f(xt)
#         print("{:.6f} = f({:.6f})".format(fc,xt))
#         print("f(xt) = {:.6f}".format(fc))
#         if fc == 0:
#             print("Langkah 5a: f(xt) = 0, akar persamaan ditemukan!")
#             return xt
#         elif fc*fa < 0:
#             print("Langkah 5b: f(xt) dan f(x1) memiliki tanda yang berlawanan, perbarui x2 = xt")
#             x2 = xt
#             fb = fc
#         else:
#             print("Langkah 5c: f(xt) dan f(x2) memiliki tanda yang berlawanan, perbarui x1 = xt")
#             x1 = xt
#             fa = fc
#         df.loc[iterasi] = [iterasi, x1, x2, xt, fa, fb, fc]
#         print("Iterasi {}: xn = {:.6f}, xn+1 = {:.6f}, xt = {:.6f}, f(xn)= {:.6f}, f(xn+1)= {:.6f}, f(xt) = {:.6f}".format(iterasi, x1, x2, xt,f(x1), f(x2), fc))
#     print("Langkah 6: Akar persamaan ditemukan!")
#     df.loc[iterasi] = [iterasi, x1, x2, xt,fa, fb, fc]
#     print("Akar persamaan: {:.6f}".format(xt))
#     print(df)
#     return xt

# # contoh penggunaan
# x = input("input persamaan : ")
# x1 = int(input("Input Xn : "))
# x2 = int(input("Input Xn+1 : "))
# tol = float(input("Inputkan Toleransi : "))
# root = bisection(x1, x2, tol)
# fx = f(x)
# print("Akar persamaan: {:.6f}".format(root))


import pandas as pd
import tkinter as tk

# fungsi untuk menampilkan output di GUI
def print_output(output):
    # output_text.delete('1.0', tk.END) # menghapus output sebelumnya
    output_text.insert(tk.END, output) # menampilkan output baru
    
def f(x):
    x_soal = x
    # x_hasil = x_hasil
    # print(x_hasil)
    return x_soal

def bisection(x1, x2, tol):
    iterasi = 0
    print_output("Metode Bisection\n")
    # output_text.delete('1.0', tk.END) # menghapus output sebelumnya
    print_output("Metode Bisection\n")
    print_output("Langkah 1: Tentukan tebakan awal x1 dan x2, serta toleransi error tol\n")
    print_output(f"x1 = {x1:.6f}, x2 = {x2:.6f}, tol = {tol:.6f}\n")
    print_output("Langkah 2: Hitung f(x1) dan f(x2)\n")
    fa = f(x1)
    fb = f(x2)
    # print_output(fb)
    print_output(f"f(x1) = {fa:.6f}, f(x2) = {fb:.6f}\n")
    df = pd.DataFrame(columns=['Iterasi', 'x1', 'x2', 'xt', 'f(x1)','f(x2)', 'f(xt)'])
    df.loc[iterasi] = [iterasi, x1, x2, None, fa, fb ,None]
    print_output(f"Iterasi {iterasi}: xn = {x1:.6f}, xn+1 = {x2:.6f}, f(x1) = {fa:.6f}, f(x2) = {fb:.6f}\n")
    while abs(x2 - x1) > tol:
        iterasi += 1
        print_output(f"Langkah 3: Hitung iterasi ke {iterasi}\n")
        xt = (x1 + x2) / 2
        print_output(f"xt = ({x1:.6f} + {x2:.6f}) / 2\n")
        print_output(f"xt = {xt:.6f}\n")
        fc = f(xt)
        print_output(f"{fc:.6f} = f({xt:.6f})\n")
        print_output(f"f(xt) = {fc:.6f}\n")
        if fc == 0:
            print_output("Langkah 5a: f(xt) = 0, akar persamaan ditemukan!\n")
            return xt
        elif fc*fa < 0:
            print_output("Langkah 5b: f(xt) dan f(x1) memiliki tanda yang berlawanan, perbarui x2 = xt\n")
            x2 = xt
            fb = fc
        else:
            print_output("Langkah 5c: f(xt) dan f(x2) memiliki tanda yang berlawanan, perbarui x1 = xt\n")
            x1 = xt
            fa = fc
        df.loc[iterasi] = [iterasi, x1, x2, xt, fa, fb, fc]
        print_output(f"Iterasi {iterasi}: xn = {x1:.6f}, xn+1 = {x2:.6f}, xt = {xt:.6f}, f(xn)= {fa:.6f}, f(xn+1)= {fb:.6f}, f(xt) = {fc:.6f}\n")
    result_label.config(text="Langkah 6: Akar persamaan ditemukan!\nAkar persamaan: {:.6f}".format(xt))
    df.loc[iterasi] = [iterasi, x1, x2, xt, fa, fb, fc]
    print_output(df)
    return xt, df

def run_bisection():
    x = str(x_entry.get())
    x_hasil = str(x_entry.get())
    x1 = float(x1_entry.get())
    x2 = float(x2_entry.get())
    tol = float(tol_entry.get())
    root, df = bisection(x1, x2, tol)
    fx= f(x)
    # result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, str(df))
    result_text.insert(tk.END, "Akar persamaan: {:.6f}".format(root, fx))

root = tk.Tk()
root.title("Metode Bisection")

# input fields
x_label = tk.Label(root, text="Fungsi f(x)")
x_label.grid(row=0, column=0)
x_entry = tk.Entry(root)
x_entry.grid(row=0, column=1)

x1_label = tk.Label(root, text="x1")
x1_label.grid(row=1, column=0)
x1_entry = tk.Entry(root)
x1_entry.grid(row=1, column=1)

x2_label = tk.Label(root, text="x2")
x2_label.grid(row=2, column=0)
x2_entry = tk.Entry(root)
x2_entry.grid(row=2, column=1)

tol_label = tk.Label(root, text="Toleransi Error")
tol_label.grid(row=3, column=0)
tol_entry = tk.Entry(root)
tol_entry.grid(row=3, column=1)

# run button
run_button = tk.Button(root, text="Run", command=run_bisection)
run_button.grid(row=4, column=1)

# result label and text box
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

result_text = tk.Text(root)
result_text.grid(row=5, column=0, columnspan=2)

output_text = tk.Text(root)
output_text.grid(row=5, column=0, columnspan=2)

root.mainloop()
