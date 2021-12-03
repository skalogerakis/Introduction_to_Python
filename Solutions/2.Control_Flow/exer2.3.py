"""
    Simple while loops
    Author: Stefanos Kalogerakis
    Last Modified: 22/10/2021
"""



# Instead of using a for loop, use a while loop to:
# (a) Print the numbers 0 to 100
# (b) Print the numbers 0 to 100 that are divisible by 7


print('Question a')

counter = 0

while(counter<=100):
	print(counter)
	counter+=1


print('\n\nQuestion b')

counter2 = 0
while(counter2<=100):
	if(counter2 % 7 == 0):
		print(counter2)
	counter2+=1
