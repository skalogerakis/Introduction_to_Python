"""
    Get method
    Author: Stefanos Kalogerakis
    Last Modified: 03/12/2021
"""

# Exercise 6.3: Get method
# Dictionaries have a get method, which takes a key and a default value. If the key is in the dictionary,
# it returns the value, otherwise, it returns the default value.
# Rewrite your code from the previous problem to make use of this get method

lst = ['x','y','z','x','x','x','y', 'z']
dct = {}


# Very simple in this case. Get sets a default value. So in that case, I can just start from
# zero in the baseline case and just increment by one
for i in lst:
    dct[i] = dct.get(i,0) + 1
    
print(dct)