# PEMROGRAMAN LANJUTAN
# KAMIS 20 JANUARI 2022

#CONTOH FUNGTION
""" def greet(name):
    print("Hello, " + name + ". Selamat Pagi")

greet('Enisda') """

""" # CONTOH PENGGUNAAN FUNGSI DENGAN RETURN
def kotak(s):
    luas = s * s
    return luas
print(kotak(10)) """

# CONTOH FUNGSI PRESENTASE
""" def persentase (total, jumlah):
    if (total>= 0 and total <= jumlah):
        return total / jumlah * 100
    return False
print(persentase(30, 60))
print(persentase(100, 60)) """

# FUNGSI REKUSIF
def tampilkanAngka (batas, i = 1):
    print(f'Perulangan ke (i)')
    if (i<batas):
        tampilkanAngka(batas, i + 1)
tampilkanAngka(10)