"""
    Printing a dictionary
    Author: Stefanos Kalogerakis
    Last Modified: 03/12/2021
"""

# Exercise 6.1: Printing a dictionary
# Write a function that prints key-value pairs of a dictionary.

dict = {1:"Stefanos", 2:"Giorgos", 4: "Antonis"}

for index, val in dict.items():
    print("The index is ",index, " and the value is ", val)