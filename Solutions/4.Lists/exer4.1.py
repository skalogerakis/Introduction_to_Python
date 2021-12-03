
"""
    Short Questions
    Author: Stefanos Kalogerakis
    Last Modified: 20/11/2021
"""

# Exercise 4.1: Short questions
# (a) Write a function that prints the elements of a list
# (b) Write a function that prints the elements of a list in reverse
# (c) Write your own implementation of the len function that returns the number of elements in a list.

print("Question a")

tst_list = [1,2,3,55,32,211]

def print_fun(lst):
	for i in lst:
		print(i)

# Call the function to test it. For the purposes of this exercice don't return anything just print out stuff
print_fun(tst_list)

print("Question b")

# Implementation using built-in function
def print_rev_lst(lst):
    for i in reversed(lst):
        print(i)

print_rev_lst(tst_list)


# Implementation using slice function
def print_rev_lst_slice(lst):
    return lst[::-1]

print(print_rev_lst_slice(tst_list))

# Implementation using a traditional approach
def print_rev_lst_trad(lst):
    for i in range(len(lst)-1, -1,-1):
        print(lst[i])
        
print_rev_lst_trad(tst_list)

print("Question c")

def custom_len(lst):
	counter = 0

	for i in range(len(lst)):
		counter+=1

	return counter

print(custom_len(tst_list))