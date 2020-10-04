'''
Created on 10/11/2019
@author:   Benjamin Singleton
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

#325 bits is largest number of bits a program could use to encode a 64-bit string if
#that string start with 1 and alternated between 1 and 0 every.


def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n==0:
        return False
    elif n%2==0:
        return False
    else:
        return True

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

def numToBinaryPad(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n
    and adds additional leading zeros as necessary according to OMPRESSED_BLOCK_SIZE.
    Intended for numbers 0 through 64, will take larger.'''
    s = numToBinary(int(n))
    return '0' * (COMPRESSED_BLOCK_SIZE - len(s))+ s

def compress_helper_num(n):
    '''Obtains the amount of times that 1 or 0 occurs consecutively'''
    if len(n)==1:
        return 1
    elif n[0]!=n[1]:
        return 1
    else:
        return 1+compress_helper_num(n[1:])

def compress(n):
    '''Takes in a binary number and returns the run-length encoding of that string'''
    def compress_helper(n, x):
        if n=='':
            return ''
        if n[0] != chr(x+ord('0')):
            return numToBinaryPad('0')+compress_helper(n, 1-x)
        else:
            length=compress_helper_num(n)
            length=min(length, MAX_RUN_LENGTH)
            return numToBinaryPad(length)+compress_helper(n[length:], 1-x)
    return compress_helper(n, 0)


def uncompress(c):
    '''Takes in a run-length encoded binary string and returns the unecoded string'''
    if c=='':
        return ''
    else:
        return (binaryToNum(c[0:5])*'0')+(binaryToNum(c[5:10])*'1')+uncompress(c[10:])
        
def compression(s):
    '''Returns the ratio of the compressed binary string vs its original uncompressed length'''
    return len(compress(s))/(len(s))

#Such an algorithm cannot exist because to compress an image without dataloss there will always be
#situations in which the length of the output string is longer than what is input. Specifically,
#the output of binary strings in which every value of the string switchs between 0 and 1 will
#always be longer have a longer output than their input.


#mainly used binary to number
#base case is the same
#if length is compressed string is equal to compressed block size,
#turn that compressed string into binary and add additional zeros
#Since compress block size is five, convert
#binarynum of first five numbers binarytonum(c[0:5])*'0'
#from digit six to digit ten binarytonum(c[5:10])*'1'
#Call function from the nedt five
#+uncompress(n[10:])


#Compress is the compress/length of string
