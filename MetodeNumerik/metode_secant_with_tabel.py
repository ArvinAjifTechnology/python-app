import pandas as pd

def f(x):
    # return x**3 +x**2-3*x-3
    # print("     2({:.6f})^3+2{:.6f}^2-2({:.6f})".format(x,x,x))
    # return 2*x**3+2*x**2-2*x
    print("({:.6f})^3+6{:.6f}-3)".format(x,x,x))
    return x**3+6*x-3

def secant(x0, x1, tol):
    iterasi = 0
    print("Metode Secant")
    print("Langkah 1: Tentukan tebakan awal x0 dan x1, serta toleransi error tol")
    print("x0 = {:.6f}, x1 = {:.6f}, e = {:.6f}".format(x0, x1, tol))
    print("Langkah 2: Hitung f(x0) dan f(x1)")
    fx0 = f(x0)
    fx1 = f(x1)
    print("f(x0) = {:.6f}, f(x1) = {:.6f}".format(fx0, fx1))
    df = pd.DataFrame(columns=['Iterasi', 'x0', 'x1', 'f(x0)', 'f(x1)', 'x2','f(x2)'])
    # df.loc[iterasi] = [iterasi,x0,x1, f(x0), f(x1),x2, fx2]
    while abs(x1 - x0) > tol:
        iterasi += 1
        print("     Langkah 3.{}: Hitung iterasi ke-{}".format(iterasi, iterasi))
        if fx1 != fx0:
            x2 = x1 - (fx1*(x1-x0))/(fx1-fx0)
            print("     x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))")
            print("     x2 = {:.6f} - ({:.6f}*({:.6f}-{:.6f}))/({:.6f}-{:.6f})".format(x1,fx1,x1,x0,fx1,fx0))
        else:
            x2 = (x0+x1)/2
            print("     x2 = (x0+x1)/2")
            print("     x2 = ({:.6f}+{:.6f})/2".format(x0,x1))
        print("     x2 = {:.6f}".format(x2))
        print("     Langkah 4: Hitung f(x2)")
        fx2 = f(x2)
        print("     f(x2) = {:.6f}".format(fx2))
        df.loc[iterasi] = [iterasi,x0,x1, f(x0), f(x1),x2, fx2]
        print("     Iterasi {}: x0 = {:.6f}, x1 = {:.6f},f(x0)=,{:.6f} ,f(x1)= {:.6f}, x2 = {:.6f}, f(x2) = {:.6f}".format(iterasi, x0, x1, f(x0), f(x1), x2, fx2))
        x0 = x1
        x1 = x2
        fx0 = fx1
        fx1 = fx2
    print("Langkah 5: Akar persamaan ditemukan!")
    df.loc[iterasi] = [iterasi,x0,x1, f(x0), f(x1),x2, fx2]
    print(df)
    return x2

# contoh penggunaan
x0 = 0
x1 = 1
tol = 0.0001
root = secant(x0, x1, tol)
print("Akar persamaan: {:.6f}".format(root))

