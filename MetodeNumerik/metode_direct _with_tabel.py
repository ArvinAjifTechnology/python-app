import pandas as pd
def g(x):
    # return (3*x+3)/(x**2+1)
    # return (-(x**2)+3*x+3)**(1/3)
    return ((x**2) + (x*x) + (x**2 + 6))**(1/3)
    # return x**3+x**2-3*x-3

def direct_iteration(x0, tol):
    iterasi = 0
    print("Metode Iterasi")
    print("Langkah 1: Tentukan tebakan awal x0 dan toleransi error tol")
    print("x0 = {:.6f}, e = {:.6f}".format(x0, tol))
    print("Langkah 2: Hitung g(x0)")
    gx0 = g(x0)
    print("g(x0) = {:.6f}".format(gx0))
    df = pd.DataFrame(columns=['Iterasi', 'x0', 'g(x0)', 'x1', 'g(x1)', 'ε'])
    while True:
        iterasi += 1
        print("     Langkah 3.{}: Hitung tebakan baru x1".format(iterasi))
        x1 = g(x0)
        print("     x1 = g(x0) = (3*x0+3)/(x0^2+1)")
        print("     x1 = {:.6f}".format(x1))
        print("     Langkah 4: Hitung g(x1)")
        gx1 = g(x1)
        print("     g(x1) = {:.6f}".format(gx1))
        e = abs((x1 - x0) / x1) * 100
        df.loc[iterasi] = [iterasi, x0, gx0, x1, gx1, e]
        print("     Iterasi {}: x0 = {:.6f}, g(x0) = {:.6f}, x1 = {:.6f}, g(x1) = {:.6f}, e = {:.6f}%".format(iterasi, x0, gx0, x1, gx1, e))
        if e <= tol:
            break
        x0 = x1
        gx0 = gx1
    print("Langkah 5: Akar persamaan ditemukan!")
    print(df)
    return x1

# contoh penggunaan
x0 = 1
tol = 0.0001
root = direct_iteration(x0, tol)
print("Akar persamaan: {:.6f}".format(root))

