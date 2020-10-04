'''
Created on 9/16/2019
@author:   Benjamin Singleton & Nicholas Soriano
Pledge:    I pledge my honor that I have abided by the Stevens' Honor System

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def letterScore(letter, scorelist):
    """Returns the score of a letter based on a list of letters and their scores"""
    if scorelist==[]:
        return []
    elif letter==scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    """Returns the scores of entire words based on added values from letterScore"""
    if S=='' or S=="":
        return 0
    else:
        return letterScore(S[0], scorelist)+(wordScore(S[1:], scorelist))

def scoreList(Rack):
    """Returns a list of words and their scores that can be made based on a rack and dictionary"""
    return map(lambda word: [word, wordScore(word, scrabbleScores)], listOfWords(Dictionary, Rack))

def bestWord(Rack):
    """Returns the highest word which can be made from a Rack based on dictionary"""
    L=scoreList(Rack)
    if L==[]:
        return ['', 0]
    IL=map(lambda X: X[1], L)
    bestScore=max(IL)
    return L[ind(bestScore, IL)]

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

def listOfWords(Dictionary, Rack):
    """Returns a list of words which can be made based on a rack"""
    return filter(lambda word: isPossible(word, Rack), Dictionary)

def remove(e, L):
    """Removes e from a list L"""
    if L==[]:
        return []
    elif L[0]==e:   
        return L[1:]
    else:
        return [L[0]]+remove(e, L[1:])

def isPossible(word, Rack):
    "Returns true if the word can be made from the rack"""
    if word=='' or word=="":
        return True
    elif word[0] in Rack: 
        return isPossible(word[1:], remove(word[0], Rack))
    else:
        return False    

