"""
    Filter
    Author: Stefanos Kalogerakis
    Last Modified: 20/11/2021
"""


# Exercise 4.7: Filter
# In lecture we have seen how to implement map using list comprehensions. Implement filter using list
# comprehensions. Name your functions myfilter so you can compare with Python’s standard filter.

k = range(8)

# My_filter implementation using comprehensions
def my_filter(f,xs):
    return [x for x in xs if f(x) == True]   

# Remind to yourself how the original filter function works.  Must convert to list first and then print
fres = list(my_filter(lambda x : x % 2 == 0 , k))
print(fres)