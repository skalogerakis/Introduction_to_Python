
"""
    Zip
    Author: Stefanos Kalogerakis
    Last Modified: 03/12/2021
"""

# Exercise 5.2: Zip
# Suppose we have two lists, x and y that give the x and y coordinates of a set of points. Create a list
# with the coordinates (x,y) as a tuple. Hint: Find out about the zip function.
# 
# You have decided that actually, you need the two seperate lists, but unfortunately, you have thrown
# them away. How can we use zip to unzip the list of tuples to get two lists again?


x = [1,32,3.2,2]
y = [2,33,12.1,4]

result = list(zip(x,y))
print("Zipping two lists", result)

# Unzip to multiple lists
inverse_zip = list(zip(*result))

# Get the x and y coordinates from the unzip
x_reverse = inverse_zip[0]
y_reverse = inverse_zip[1]
print(x_reverse)
print(y_reverse)
