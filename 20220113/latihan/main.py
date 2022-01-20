# ENISDA LIBRA KELANA
# 11203462010011

# programing language = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
# using for loop and print out the item
# after that reverse the order with loop not with function called reversed()

# LIST PROGRAMING LANGUAGE
programingLanguage = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

# PRINT LIST USING FOR LOOP
for i in programingLanguage:
    print(i)

# PRINT REVERSED LIST USING FOR LOOP 
reversed_list = []
for i in range(len(programingLanguage)):
    reversed_list.append(programingLanguage.pop())
print(reversed_list)

# PRINT REVERSED LIST USING WHILE LOOP
""" i = len(programingLanguage) - 1 
while i >= 0 :
    print(programingLanguage[i]) 
    i -= 1 """