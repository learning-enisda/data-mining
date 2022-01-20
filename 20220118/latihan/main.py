# makes python program that multiply  all thr integer in the list
# example:
# if i have a list: list=[1,2,3,4]
# then the output must be 1*2*3*4 = 24

""" logic
print(1*1)
print(1*2)
print(2*3)
print(6*4) """

""" a = [1, 2, 3, 4]
b = 1
for x in a:
    b = b * x
print(b)

a = [1, 2, 3, 4]
b = 0
for x in a:
    b = b + x
print(b) """

# make a combination of initial value:
""" from itertools import combinations


dict_1 = {1:5,2:4}
dict_2 = {1:2,1:4}
dict_3 = {1:4,2:9} """


""" # Python3 code to demonstrate working of
# Dictionary key combinations
# Using itertools.combinations()
import itertools

# Initializing dict
test_dict = {'gfg' : 1, 'is' : 2, 'the' : 3, 'best' : 4}

# printing original dict
print("The original dict is : " + str(test_dict))

# Dictionary key combinations
# Using itertools.combinations()
res = list(itertools.combinations(test_dict, 2))

# printing result
print("The dictionary key pair list is : " + str(res)) """


import itertools
dict_1 = {1:5,2:4}
dict_2 = {1:2,1:4}
dict_3 = {1:4,2:9}
""" dict_4 = [dict_1,dict_2, dict_3]
list(itertools.product(*dict_4))
print(dict_4) """

#

for i in itertools.combinations(range(2500), 3):
    print(i)



# Python3 code to demonstrate
# to compute all possible permutations
# using list comprehension

# initializing lists
list1 = [1, 3, 4]
list2 = [6, 7, 9]
list3 = [8, 10, 5]

# printing lists
print ("The original lists are : " + str(list1) +
							" " + str(list2) +
							" " + str(list3))

# using list comprehension
# to compute all possible permutations
res = [[i, j, k] for i in list1
				for j in list2
				for k in list3]

# printing result
print ("All possible permutations are : " + str(res))
