#This notebook is a solution to Euler problem ID 4: Largest Palindrome Product.
#Link: https://projecteuler.net/problem=4

#Import libraries
import numpy as np
import pandas as pd
#-----------------------------------------------------------------------------------------------------------------------------------

def is_palindrome(n):
    """Function to identify if a number n is a palindrome or not.
    If yes, return True, if not return False."""

    n_s = str(n) #make n a string to be able to extract characters.
    l = len(n_s)
    n_v=[]       #define a list to store characters of n

    for i in range(l): #build list of characters
         n_v.append(n_s[i])

    n_r=[]       #build reversed list
    for i in range(l): 
         n_r.append(n_s[-i-1])
    
    if n_v==n_r: #check for palindrome
        return n
    else:
        return 0


s = [] #list of candidates
for i in range(999,99,-1):
    for j in range(i,99,-1):
        n = i*j
        s.append(n)

output = list(map(is_palindrome,s)) #check if palindrome
max(output)