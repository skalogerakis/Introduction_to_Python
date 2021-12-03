
"""
    Distances
    Author: Stefanos Kalogerakis
    Last Modified: 03/12/2021
"""

# Exercise 5.3: Distances
# Suppose we have two vectors, x and y, stored as tuples with n elements. Implement functions that
# compute the l1 and l2 distances between x and y. Note that n is not explicitly given.

# Sources for the distance theory l1, l2 https://www.cs.utah.edu/~jeffp/teaching/cs5955/L7-Distances.pdf
# L1 is called the Manhattan distance, and is ManhattanDistance = sum for i to N sum |x[i] – y[i]|

# L2 is the Euclidian distance and is the sqrt(sum for i to N (x[i] – y[i])^2)


import math
x = [10, 20, 15, 10, 5]
y = [12, 24, 18, 8, 7]

# Suppose we have two vectors, x and y, stored as tuples with n elements. Implement functions that
# # compute the l1 and l2 distances between x and y. Note that n is not explicitly given

def manhattan_distance(a, b):
	return sum(abs(e1-e2) for e1, e2 in zip(a,b))
	
	
print("The manhattan_distance is :", manhattan_distance(x,y))

def euclidean_distance(a, b):
	return math.sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))
	
print("The euclidean_distance is: ", euclidean_distance(x,y))