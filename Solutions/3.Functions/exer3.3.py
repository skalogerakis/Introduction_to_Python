"""
    Maximum
    Author: Stefanos Kalogerakis
    Last Modified: 22/10/2021
"""



# Write a function my_max(x,y) that returns the maximum of x and y. Do not use the max function, but
# use if instead in following two ways:
# (a) Use both if and else.
# (b) Use if but not else (nor elif).


def my_max_a(x,y):
	if x > y:
		return x
	else:
		return y



def my_max_b(x,y):
	if x > y:
		return x
	return y


value1 = 10
value2 = 24

print('The max value out of ',value1, ' and  ', value2, ' is: ', my_max_a(value2,value1))
print('The max value out of ',value1, ' and  ', value2, ' is: ', my_max_b(value2,value1))