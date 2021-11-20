"""
    Lists and functions
    Author: Stefanos Kalogerakis
    Last Modified: 20/11/2021
"""


# Exercise 4.4: Lists and functions
# Write a function that takes a list and an index, and sets the value of the list at the given index to 0

a = [1,24,23,2,1,2]

# Consider that the index starts from 0
def index_mod(lst, index):
    lst[index] = 0
    return lst
    
print("Initial List ", a)
print("Modified index list ", index_mod(a,3))