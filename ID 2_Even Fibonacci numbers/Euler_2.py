#This notebook is a solution to Euler problem ID 2: Even Fibonacci numbers.
#Link: https://projecteuler.net/problem=2

#Import libraries
import numpy as np
import pandas as pd
#-----------------------------------------------------------------------------------------------------------------------------------

def fibonacci(n):
    """Function that returns an array of fibonacci
    numbers smaller than n."""

    #initialize array
    a = np.arange(3)
    while a[-1] < n:
        a = np.append(a,a[-1]+a[-2])
    a = a[0:-1] #remove last number
    return a

def even(x):
    """Function that returns zero if x is odd and x if x is even"""

    if x % 2 == 0 :
        return x
    return 0

#vectorize even function
even_v = np.vectorize(even)

fs = even_v(fibonacci(4000000.)).sum()
print(fs)
