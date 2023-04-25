import pandas as pd

def f(x):
    # return x**3-7*x+1
    # return x**3+x**2-3*x-3
    print("({:.6f})^3+6{:.6f}-3)".format(x,x,x))
    # return 2*x**3+2*x**2-2*x
    return x**3+6*x-3

def regulafasi(x0, x1, tol):
    iterasi = 0
    print("Metode Regulafasi")
    print("Langkah 1: Tentukan tebakan awal x0 dan x1, serta toleransi error tol")
    print("x0 = {:.6f}, x1 = {:.6f}, tol = {:.6f}".format(x0, x1, tol))
    print("Langkah 2: Hitung f(x0) dan f(x1)")
    fx0 = f(x0)
    fx1 = f(x1)
    print("f(x0) = {:.6f}, f(x1) = {:.6f}".format(fx0, fx1))
    # df = pd.DataFrame(columns=['Iterasi', 'xn', 'xn+1', 'xt', 'f(xn)','f(xn+1)', 'f(xt)'])
    print("Iterasi {}: x0 = {:.6f}, x1 = {:.6f}, f(x0) = {:.6f}, f(x1) = {:.6f}".format(iterasi, x0, x1, fx0, fx1))
    # df.loc[iterasi] = [iterasi, x0, x1, None, fx0, fx1 ,None]
    while abs(x1 - x0) > tol:
        iterasi += 1
        print("Langkah 3: Hitung iterasi ke-{}".format(iterasi))
        xt = (x0*fx1 - x1*fx0) / (fx1 - fx0)
        # df.loc[iterasi] = [iterasi, x0, x1, xt, f(x0), f(x1) ,f(xt)]
        print("xt = (x0*fx1 - x1*fx0) / (fx1 - fx0)")
        print("xt = ({:.6f}*f({:.6f}) - {:.6f}*f({:.6f})) / (f({:.6f}) - f({:.6f}))".format(x0,fx1,x1,fx0,fx1,fx0))
        print("xt = {:.6f}".format(xt))
        print("Langkah 4: Hitung f(xt)")
        fc = f(xt)
        print("f(xt) = {:.6f}".format(fc))
        if fc*fx1 < 0:
            print("Langkah 5a: f(xt) dan f(x1) memiliki tanda yang berlawanan, perbarui x0 = xt")
            x0 = xt
            fx0 = fc
        else:
            print("Langkah 5b: f(xt) dan f(x0) memiliki tanda yang berlawanan, perbarui x1 = xt")
            x1 = xt
            fx1 = fc
        print("Iterasi {}: xn = {:.6f}, xn+1 = {:.6f}, xt = {:.6f}, f(xn)={:.6f} ,f(xn+1) ={:.6f},f(xt) = {:.6f}".format(iterasi, x0, x1, xt,f(x0), f(x1) , fc))
    print("Langkah 6: Akar persamaan ditemukan!")
    # df.loc[iterasi] = [iterasi, fx0, fx1, xt, f(x0), f(x1) ,f(xt)]
    # print(df)
    return xt

# contoh penggunaan
x0 = 0
x1 = 1
tol = 0.0001
root = regulafasi(x0, x1, tol)
print("Akar persamaan: {:.6f}".format(root))



