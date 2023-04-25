import pandas as pd
#from tabulate import tabulate
import numpy as np
# import matplotlib.pyplot as plt

def f(x):
    # return x**3-7*x+1
    # return x**3 +x**2-3*x-3
    # print("2({:.6f})^3+2{:.6f}^2-2({:.6f})".format(x,x,x))
    # return 2*x**3+2*x**2-2*x
    # print("({:.6f})^3+6{:.6f}-3)".format(x,x,x))
    # return x**3+6*x-3
    print("({:.6f})^3-7{:.6f}+1)".format(x,x,x))
    return x**3-7*x+1


def dfx(x):
    return 3*x**2 - 7
    # return 3*x**2 + 6

def newton(x0, tol):
    tabel = []
    iterasi = 0
    print("Metode Newton")
    print("Langkah 1: Tentukan tebakan awal x0 dan toleransi error tol")
    print("x0 = {:.6f}, tol = {:.6f}".format(x0, tol))
    while True:
        iterasi += 1
        print("Langkah 2: Hitung f(x) dan f'(x)")
        fx = f(x0)
        df = dfx(x0)
        print("f(x) = {:.6f}, f'(x) = {:.6f}".format(fx, df))
        if abs(fx) <= tol:
            print("Langkah 4: Akar persamaan ditemukan!")
            return x0
            # break
        x1 = x0 - fx / df
        print("Iterasi {}: x0 = {:.6f}, f(x0) = {:.6f}, x1= {:.6f} , f(x1) = {:.6f}, f'(x0) = {:.6f}".format(iterasi, x0, fx,x1,f(x1), df))
        tabel.append([iterasi, x0, fx,x1,f(x1), df])
        print("x1 = {:.6f} - {:6f} / {:.6f}".format(x0,fx,df))
        print("Langkah 3: Hitung tebakan baru x1")
        print("x1 = x0 - f(x0) / f'(x0)".format(x1))
        print("x1 = {:.6f} - f({:.6f}) / f'({:6f}) = {:.6f}".format(x0,fx,df,x1))
        if abs(x1 - x0) <= tol:
            print("Langkah 4: Akar persamaan ditemukan!")
            return x1
        x0 = x1
    # return x0
        
    # dfr = pd.DataFrame(columns=['Iterasi', 'x0', 'f(x0)', 'x1', 'f(x1)', "f'(x0)"])    

# contoh penggunaan
x0 = 1
tol = 0.0001
print(f"x0= {x0}")
print(f"e= {tol}")
# root, x1,tabel = newton(x0, tol)
root = newton(x0, tol)
print("Akar persamaan: {:.6f}".format(root))
# print(tabulate(tabel, headers=['Iterasi', 'x0', 'f(x0)', 'x1', 'f(x1)', "f'(x0)"]))