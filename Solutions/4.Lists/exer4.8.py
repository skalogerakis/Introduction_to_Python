"""
    Flatten a list of lists
    Author: Stefanos Kalogerakis
    Last Modified: 20/11/2021
"""


# Exercise 4.8: Flatten a list of lists
# Consider having a list with lists as elements, e.g. [[1,3], [3,6]].
# Write a function that takes such a list, and returns a list with as elements the elements of the sublists,
# e.g. [1, 3, 3, 6].

lst = [[1,3], [3,6]]

def flatten_custom(lst):
    ret_lst = []    # Initialize a new list to add the desired elements

    for x in lst:   # Iterate through the initial list 
        for y in x: # Iterate now to the list of sublists
            ret_lst.append(y)   # Add all the elements one by one to the new list
    return ret_lst
        
print(flatten_custom(lst))



