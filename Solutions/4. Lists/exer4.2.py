
"""
    Copying Lists
    Author: Stefanos Kalogerakis
    Last Modified: 20/11/2021
"""

# (a) Create a list a with some entries
# (b) Now set b = a
# (c) Change b[1]
# (d) What happened to a?
# (e) Now set c = a[:]
# (f) Change c[2]
# (g) What happened to a?
# Now create a function set_first_elem_to_zero(l) that takes a list, sets its first entry to zero, and
# returns the list.
# What happens to the original list?


# Execute it yourself to figure out what is going on
a = [1,24,23,2,1,2]

print(a)

b = a

print(b)

b[1] = 99

print(a)

c = a[:]

print(c)

c[2]= 333

print(a)
print(c)


def set_first_elem_to_zero(l):
    l[0] = 0
    return l
    
print(set_first_elem_to_zero(c))
