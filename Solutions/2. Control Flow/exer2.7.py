"""
    Collatz sequence
    Author: Stefanos Kalogerakis
    Last Modified: 22/10/2021
"""


# A Collatz sequence is formed as follows: We start with some number x0, and we find the next number
# in the sequence by
#          \
# x_i+1 => \    x_i/2,          if x_i is even
#          \    3*x_i + 1       if x_i is odd
#          \
# If xi = 1, we stop iterating and have found the full sequence.
# For example, if we start with x0 = 5, we obtain the sequence:
# 5 16 8 4 2 1
#
# x0 = 5
# x1 = 3 * x0 + 1 = 16
# x2 = x1/2 = 8
# x3 = x2/2 = 4
# x4 = x3/2 = 2
# x5 = x4/2 = 1

# It is conjectured, though not proven, that every chain eventually ends at 1.
# Print the Collatz sequence starting at x0 = 103.


number = 103
counter = 0

while number != 1:
    counter += 1
    print('The ', counter, ' element of the sequence is ',int(number))
    if(number%2==0):
        number = number / 2
    else:
        number = 3*number + 1

    if number == 1: print('The last element of the sequence is ', int(number))
