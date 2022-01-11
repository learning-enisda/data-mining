# perulangan Python (python loop)
# for, while, & fungsi refusif

""" # Program 1 
listKota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi','Solo', 'Jogjakarta', 'Semarang', 'Makassar'
]
for kota in listKota:
    print(kota)

# Program 2
listKota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi','Solo', 'Jogjakarta', 'Semarang', 'Makassar'
]
for i in enumerate (listKota):
    print(i, kota)

# For dengan Range (For in Range)
# Contoh Perulangan dari 0 sampai 4
for i in range(5):
    print("Perulangan ke -", i)
# Contoh Perulangan dari 10 sampai 15
for i in range(10, 16):
    print('i =', i) """

#
listKota = [
'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
'Jogjakarta', 'Semarang', 'Makassar'
]
kotaYangDicari = input('Ketik nama kota yang kamu cari: ')
for i, kota in enumerate(listKota):
    if kota.lower() == kotaYangDicari.lower():
        print('Kota yang anda cari berada pada indeks', i)
        break
    else:
        print('Maaf, kota yang anda cari tidak ada')