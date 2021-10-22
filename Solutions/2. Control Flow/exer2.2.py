"""
    For loops
    Author: Stefanos Kalogerakis
    Last Modified: 22/10/2021
"""



#Use a for loop to:
#	(a) Print the numbers 0 to 100
#	(b) Print the numbers 0 to 100 that are divisible by 7
#	(c) Print the numbers 1 to 100 that are divisible by 5 but not by 3
#	(d) Print for each of the numbers x = 2, . . . 20, all numbers that divide x, excluding 1 and x. Hence, for 18, it should print 2 3 6 9.


print('Question a')

for i in range(101):
	print(i)


print('\n\nQuestion b')

for i in range(101):
	if(i % 7 == 0):
		print(i)

print('\n\nQuestion c')

for i in range(101):
	if(i % 5 == 0 and i % 3 != 0):
		print(i)


print('\n\nQuestion d')

for i in range(2,21):
	for j in range(2,21):
		if(i % j == 0 and i!=j):
			print('For number ',i,' ', j)