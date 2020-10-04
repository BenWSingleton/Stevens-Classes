#Benjamin Sinleton
#I pledge that I have abided by the Stevens Honor System

from cs115 import *

def dot(L, K):
    """Outputs the dot product of the lists L & K"""
    if L==[]:
        return 0.0
    elif K ==[]:
        return 0.0
    else:
        return L[0]*K[0]+dot(L[1:], K[1:])

def explode(s):
    """Takes a string s and returns a list of the characters"""
    if s=="" or s=='':
        return []
    else:
        return [s[0]]+explode(s[1:])

def ind(e, L):
    """Returns the index at which value e was found"""
    if L=="":
        return 0
    elif L==[]:
        return 0
    elif L[0]==e:
        return 0
    else:
        return 1+ind(e,L[1:]) 

def removeAll(e, L):
    """Removes all values e from a list L"""
    if L==[]:
        return []
    elif L[0]==e:
        return [L[1]]+removeAll(e, L[2:])
    else:
        return [L[0]]+removeAll(e, L[1:])

def even(x):
    if x%2==0:
        return True
    else:
        return False

def myFilter(f, L):
    """Returns a new list based on L in which all values for f return True"""
    if L==[]:
        return []
    elif f(L[0])==False:
        return myFilter(f, L[1:])
    else:
        return [L[0]]+myFilter(f, L[1:])
        

def deepReverse(L):
    """Returns the reveral of a list"""
    if L==[]:
        return []
    else:
        if isinstance(L[0], list):
            return deepReverse(L[1:])+[deepReverse(L[0])]
        else:
            return deepReverse(L[1:])+[L[0]]
