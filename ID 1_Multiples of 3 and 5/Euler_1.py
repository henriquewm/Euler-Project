#This notebook is a solution to Euler problem ID 1: Multiples of 3 or 5.
#Link: https://projecteuler.net/problem=1

#Import libraries
import numpy as np
import pandas as pd
#-----------------------------------------------------------------------------------------------------------------------------------

def multiples(x):
    """Function to identify if a number is a multiple of 3 or 5.
    If yes, return the input, if not return 0."""

    if (x % 3 == 0) or (x % 5 == 0) :
        return x
    return 0

#Create an array with range from 0 to n.
n=1000
a = np.arange(n+1)

#Vectorize multiples function and apply to array
multiples_v = np.vectorize(multiples)
a_m = multiples_v(a)

#apply sum to a_m
a_s = a_m.sum()
print(a_s)