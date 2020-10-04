#Benjamin Singleton
#I pledge my honor that I have abided by the Stevens honor system


from cs115 import *

import math

def mult(x, y):
    """Return the product of x & y"""
    return x*y

def factorial(n):
    """Returns n! of n"""
    list1=range(1, n+1)
    #print(list1)
    return reduce(mult, list1)

def add(x, y):
    """Returns the sum of x & y"""

def mean(L):
    """Returns the mean value of a list"""
    length=len(L)
    #print(length)
    tot=sum(L)
    #print(tot)
    return tot/length

def div(k):
    """Returns True a value K divides 42 with no remainder""" 
    return 42%k==0

def divides(n):
    def div(k):
        return n % k == 0
    return div

def prime(n):
    """Returns True if prime, false if not"""
    if n==1: return False
    #print(list1)
    if True in map(divides(n),range(2, n)):
        return False
    return True
