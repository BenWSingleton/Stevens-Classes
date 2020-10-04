from cs115 import *
import math
'''
Created on 9/21/2019
@author:   Benjamin Singleton
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    """Returns a non-negative integer indicating the minimum
    number of coins required to make up the given amount"""
    if amount==0:
        return [0, []]
    elif coins==[] or amount < 0:
        return [float("inf"), []]
    elif coins[0]>amount:
        return giveChange(amount, coins[1:])
    else:
        [use, uselist]=giveChange(amount-coins[0], coins)
        [lose, loselist]=giveChange(amount, coins[1:])
    if use+1 < lose:
        uselist.append(coins[0])
        return [use+1, uselist]
    else:
        return [lose, loselist]


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct==[]:
        return []
    else: 
        return map(lambda word: [word, wordScore(word, scores)], dct)

def wordScore(S, scorelist):
    """Returns the scores of entire words based on added values from letterScore"""
    if S=='' or S=="":
        return 0
    else:
        return letterScore(S[0], scorelist)+(wordScore(S[1:], scorelist))

def letterScore(letter, scorelist):
    """Returns the score of a letter based on a list of letters and their scores"""
    if scorelist==[]:
        return []
    elif letter==scorelist[0][0]:
        return scorelist[0][1]
    else:
        return letterScore(letter, scorelist[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n==0:
        return []
    else:
        return [L[0]]+take(n-1, L[1:])

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n==0:
        return L
    else:
        return drop(n-1, L[1:])


