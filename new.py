import itertools
semua_kamus = [[1, 3, 4], [6, 7, 9], [8, 10, 5] ]
print (str(semua_kamus))
res = list(itertools.product(*semua_kamus))
print (str(res))