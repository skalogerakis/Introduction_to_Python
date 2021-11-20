"""
    More while loops
    Author: Stefanos Kalogerakis
    Last Modified: 22/10/2021
"""



#The smallest number that is divisible by 2, 3 and 4 is 12. Find the smallest number that is divisible by
#all integers between 1 and 10.

curr_number = 1

while(True):

	range_counter = 0 	# Assign a temporary counter to keep track whether we have found the range that we wanted
	for i in range(1,11):
		range_counter+=1
		if(curr_number%i == 0):
			continue
		else:
			curr_number+=1 		# In case a value in that range fails, then go to the next number
			break

	if range_counter == 10:	# In case we have a number divided by all integers between 1 and 10 exit
		break

print(curr_number)

# Or a simpler solution

number = 1
c_range = 1
while(c_range < 11):
	if(number % c_range == 0):
		c_range+=1
	else:
		c_range=1
		number+=1

print(number)