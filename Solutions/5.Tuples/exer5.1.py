
"""
    Swapping two values
    Author: Stefanos Kalogerakis
    Last Modified: 20/11/2021
"""

# Exercise 5.1: Swapping two values
# Suppose you have two variables: a and b. Now you want to set a equal to the value of b and at the
# same time set b equal to the value of a.
# The following obviously does not work
# a = b
# b = a
# so in some languages, you need to define a third variable like this
# t = a
# a = b
# b = t
# However, in Python you don’t need to do this. How can you swap a and b in one line?

# Initialize a tuple
(a , b) = (7 , 6)

# We can simply define a tuple that takes the reverse values
(d , f) = (b , a)

print((d , f))