# use for loop to iterate from 0 to 100 an print even numbers then print only odd number


# Python program to print Even Numbers in given range
start, end = 1, 100
# iterating each number in list
for num in range(start, end):
	# checking condition
	if num % 2 == 0:
		print(num, end=" ")


# Python program to print odd Numbers in given range
start, end = 1, 100
# iterating each number
for num in range(start, end + 1):
	# checking condition
	if num % 2 != 0:
		print(num, end = " ")