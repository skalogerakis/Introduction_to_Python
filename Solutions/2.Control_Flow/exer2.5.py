"""
    While loops
    Author: Stefanos Kalogerakis
    Last Modified: 22/10/2021
"""



# Use a while loop to find the first 20 numbers that are divisible by 5, 7 and 11, and print them 
# Hint: store the number found so far in a variable.

#Pseudo-code:
#
#number found = 0
#x = 11
#while number found is less than 20:
#	if x is divisible by 5, 7 and 11:
#		print x
#		increase number found by 1
#	increase x by 1


number_found = 0
curr_number = 1

while number_found <=20:
	if (curr_number % 5 == 0) and (curr_number % 7 == 0) and (curr_number % 11 == 0):
		print(curr_number)
		number_found+=1
	curr_number+=1