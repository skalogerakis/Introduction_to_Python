"""
    Vector functions
    Author: Stefanos Kalogerakis
    Last Modified: 03/12/2021
"""

# Exercise 6.5: Vector functions
# Let’s implement some vector functions. There are two types of vectors, normal or dense vectors, which
# we can represent using lists. For sparse vectors, where many of the elements are zero, this is inefficient.
# Instead, we use a dictionary with keys the indices of non-zero values, and then the value corresponding
# to the key is the value of the vector at that index. Hence, the vector [1, 2, 4] can be stored as a list: [1,
# 2, 4] or as a dictionary {0:1, 1: 2, 2: 4}.


# (a) Write a function that adds two (dense) vectors
# (b) Write a function that multiplies (i.e. inner product) two (dense) vectors
# (c) Write a function that adds two sparse vectors
# (d) Write a function that multiplies two sparse vectors
# (e) Write a function that adds a sparse vector and a dense vector
# (f) Write a function that multiplies a sparse vector and a dense vector