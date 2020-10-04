'''
Created on 10/10/2019
@author:   Benjamin Singleton
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n==0:
        return False
    elif n%2==0:
        return False
    else:
        return True

#    42->1 0 1 0 1 0 

#If a number is even, the rightmost binary digit it zero and if it is odd,
#the right most digit is one.

#By removing the rightmost digit in a binary number, you are preforming
#integer division on that number.

#If odd add one to the right side and divide n by integer division 2.
#If even add zero to the right side and divide n by integer division 2. 

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if int(n)==0:
        return ''
    elif int(n)==1:
        return str(1)
    elif isOdd(int(n))==True:
        return numToBinary(int(n)//2)+str(1)
    else:
        return numToBinary(int(n)//2)+str(0)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    elif s[-1]==0:
        return 0
    else:
        return 2*(binaryToNum(s[:-1]))+int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s=='0':
        return str(1)
    elif s=='':
        return ''
    elif s[-1]=='0':
        return s[:-1]+str(1)
    else:
        return increment(s[:-1])+str(0)

def incrementalt(s):
    thing=binaryToNum(s)
    thing=thing+1
    return numToBinary(thing)

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints     if n=='':
        return 0s and its n successors.'''
    if n==0:
        return print(s)
    else:
        print(s)
        return count(increment(s), n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if int(n)==0:
        return ''
##    if int(n)==1:
##        return '1'
##    elif str(n%3)==0:
##        return (n//3)*numToTernary(n//3)+str((n//3))
##    else:
    return numToTernary(n//3)+str((n%3))

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    elif s[-1]==0:
        return 0
    else:
        return 3*(ternaryToNum(s[:-1]))+int(s[-1])
