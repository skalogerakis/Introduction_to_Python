"""
    Histogram
    Author: Stefanos Kalogerakis
    Last Modified: 03/12/2021
"""

# Exercise 6.2: Histogram
# Write a function that takes a list, and returns a dictionary with keys the elements of the list and as
# value the number of occurances of that element in the list.
# After you are done, look up ‘python collections counter’ in Google. Could you use a counter instead?


lst = ['x','y','z','x','x','x','y', 'z']
dct = {}

# Parse all the items in the list
for i in lst:
    # Check whether an item already exists in our dictionary
    if i in dct.keys():
        # If it exists then increment the counter by one
        dct[i] += 1
    else:
        # If it does not simply add a new entry
        dct[i] = 1
    
print(dct)

# After searching in google the counter collection, there is function that
# returns the desired result
from collections import Counter
print(Counter(lst))