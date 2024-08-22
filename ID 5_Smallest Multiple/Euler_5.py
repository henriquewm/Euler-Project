#This notebook is a solution to Euler problem ID 5: Smallest multiple.
#Link: https://projecteuler.net/problem=5

#Import libraries
import numpy as np
import pandas as pd
from collections import Counter
#-----------------------------------------------------------------------------------------------------------------------------------
def prime(n):
    """Function that returns an array with prime decomposition
    of n."""

    #initialize list to store decomposition
    a = []
    #run loop from 2 until sqrt of n to try division.
    #Smallest prime factor has to be smaller than sqrt(n) by definition
    f = 2 # initialize f with smallest prime number
    while f*f <= n:
        if n % f == 0:
            n /= f
            a.append(f)
        else:
            f +=1
    a.append(n) #if all above fails the remaining is a prime number
    return a


c=Counter()
for i in range(1,21):
    c |= Counter(prime(i))

p=1
for i in c.keys():
    p*=i**c[i]

prime(8)