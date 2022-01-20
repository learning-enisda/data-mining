# NAMA  : ENISDA LIBRA KELANA
# NIM   : 11203462010011

# MAKE A COMBINATION OF INITIAL VALUE:
""" 
kamus1 = {1:5,2:4}
kamus2 = {1:2,1:4}
kamus3 = {1:4,2:9}
"""

# METODE 1
dict_1 = {1:5,2:4}
dict_2 = {1:2,1:4}
dict_3 = {1:4,2:9}

res = [[i, j, k] for i in dict_1
                for j in dict_2
                for k in dict_3]
print("All possible : " + str(res))

# METODE 2
# using itertools.product()
import itertools
# initializing list
all_dict = [{1:5,2:4},{ 1:2,1:4}, {1:4,2:9}]
# printing lists
print ("The original dict : " + str(all_dict))
# all possible combination
res = list(itertools.product(*all_dict))
# printing result
print ("All possible combination : " + str(res))
