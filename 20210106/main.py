#ini adalah program 1
if True:
    print('Kode program akan dieskekusi')
if False:
    print('Kode tidak akan dieksekusi')
print('kode program ini akan selalu dieksekusi termasuk apda percabangan')

#ini adalah program  2
nilai = int(input('masukkan nilai anda : '))
print('nilai anda adalah:', nilai, '\'n')
if nilai >= 80:
    print ('selamat anda lulus')
else:
    print('maaf anda tidak lulus')

#ini adalah program ke 3 | Operator pada boolean
buah_yang_tersedia = ['jeruk', 'mangga', 'melon']
buah_yang_dicari = input('Masukkan nama buah dalam huruf kecil: ')
if (buah_yang_dicari in buah_yang_tersedia):
    print('Buah yang anda cari tersedia!')
else:
    print('Buah yang anda cari tidak tersedia!')

#ini adalah program 4
nilai = int(input('Masukkkan nilai : '))
usia = int(input('Masukkan usia : '))
if nilai >= 75:
    if (usia < 15):
        print('Selamat adek kamu lulus!')
    else:
        print('Selamat kakak, kamu lulus!')
else:
    if (usia < 15):
        print('Mohon maaf dek, coba lagi ya!')
    else:
        print('Mohon maaf kak, coba lagi ya!')