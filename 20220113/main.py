# DATA MINING
# KAMIS 13 JANUARI 2021

# WHILE LOOP
""" while akan membuat kode yang diulang-ulang """

""" #contoh
i = 1
while i <= 5:
    print(i)
    i += 1 """

# WHILE UNTUK LIST
listKota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Jogjakarta', 'Semarang', 'Makassar'
]
# bermain index
print('Bermain index')

i = 0
while i < len(listKota) :
    print(listKota[i])
    i += 1

""" logic:
        - python akan memeriksa apaakah and
"""

# bermain pop
print  ('Bermain POP')

"""
- Syntax: list_name.pop(index)
- Parameter: index (optional) – The value at index is popped out and removed. If the index is not given, then the last element is popped out and removed.
- Returns: The last value or the given index value from the list.
- Exception: When the index is out of range, it returns IndexError. """

listKota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Jogjakarta', 'Semarang', 'Makassar'
]
while listKota:
    print(listKota.pop(0))

# WHILE DENGAN MENGGUNAKAN CONTINUE
""" perintah continue berfungsi untuk meng-skip iterasi selanjutnya """
listKota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Jogjakarta', 'Semarang', 'Makassar'
]
i = -1
while i < len(listKota):
    i += 1
    if i % 2 == 0 and i > 0:
        print('skip')
        continue
    print(listKota[i])