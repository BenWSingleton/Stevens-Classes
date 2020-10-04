#Benjamin Singleton

from cs115 import *

import math

def dbl(x):
    """Returns twice its input x
    input x: a number (int or float)"""
    return 2*x

def doublesum(n):
    """Returns the sum 0 + 2 + ... + 2n"""
    list1=range(1, n+1)
    list2=map(dbl, list1)
    answer = sum(list2)
    return answer

def doublesum1(n):
    return sum(map(dbl, range(1, n+1)))

def doublesum2(n):
    return 2*sum(range(1,n+1))

#1
def inverse(n):
    """Returns inverse of n, duh"""
    return 1.0/n

#2
def e(n):
    """Returns calulated value of e"""
    list1=range(1, n+1)
    #print(list1)
    list2=map(math.factorial, list1)
    #print(list2)
    list3=map(inverse, list2)
    #print(list3)
    return 1+(sum(list3))

#2
def e2(n):
    """One line calculation of value of e"""
    return 1+sum(map(inverse, map(math.factorial, range(1, n+1))))

#3
def error(n):
    """Returns the difference(error) between calculated and actual e"""
    return math.e-e(n)

#I pledge my honor that I have abided by the stevens honor system
#-Benjamin Singleton
