#
# life.py - Game of Life lab
#
# Name: Benjamin Singleton
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """returns a 2d array with "height" rows and "width" cols"""
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

import sys

def printBoard(A):
    """this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def diagonalize(width, height):
    """creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells."""
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row==col:
                A[row][col]=1
            else:
                A[row][col]=0

    return A

def innerCells(w,h):
    A = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if row==0:
                A[row][col]=0
            elif col==0:
                A[row][col]=0
            elif row==(h-1):
                A[row][col]=0
            elif col==(w-1):
                A[row][col]=0
            else:
                A[row][col]=1
    return A

def randomCells(w,h):
    A = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if row!=0 and col!=0 and row!=(h-1) and col!=(w-1):
                A[row][col]=random.choice([0,1])
    return A

def copy(A):
    w=len(A[0])
    h=len(A)
    B=createBoard(w,h)
    for row in range(h):
        for col in range(w):
            B[row][col]=A[row][col]
    return B

def innerReverse(A):
    B=copy(A)
    w=len(B[0])
    h=len(B)
    for row in range(h):
        for col in range(w):
            if row!=0 and col!=0 and row!=(h-1) and col!=(w-1):
                if B[row][col]==0:
                    B[row][col]=1
                else:
                    B[row][col]=0
    return B

def next_life_generation(A):
    """Makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0."""
    B=copy(A)
    w=len(B[0])
    h=len(B)
    for row in range(h):
        for col in range(w):
            if row!=0 and col!=0 and row!=(h-1) and col!=(w-1):
                if B[row][col]==1 and countNeighbors(row, col, A)<2:
                    B[row][col]=0
                elif B[row][col]==1 and countNeighbors(row,col, A)>3:
                    B[row][col]=0
                elif B[row][col]==0 and countNeighbors(row, col, A)==3:
                    B[row][col]=1
    return B

def countNeighbors(row,col,A):
    count=0
    if A[row-1][col]==1:
        count=count+1
    if A[row+1][col]==1:
        count=count+1
    if A[row][col-1]==1:
        count=count+1
    if A[row][col+1]==1:
        count=count+1
    if A[row-1][col+1]==1:
        count=count+1
    if A[row+1][col+1]==1:
        count=count+1
    if A[row-1][col-1]==1:
        count=count+1
    if A[row+1][col-1]==1:
        count=count+1
    return count
                
