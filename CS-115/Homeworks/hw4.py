#Benjamin Singleton
#I pledge my honor that I have abided by the Stevens Honor System

from cs115 import *

def pascal_helper(row):
    """Assists pascal_row by adding the values of the previous row together"""
    if row==[]:
        return []
    if len(row)==1:
        return []
    else:
        return [row[0]+row[1]]+pascal_helper(row[1:])

def pascal_row(n):
    """Returns the n row of pascal's triangle"""
    if n==0:
        return [1]
    else:
        return [1]+pascal_helper(pascal_row(n-1))+[1]
    
def pascal_triangle(n):
    """Returns a list comprised of each row of pascal's triangle up to row n"""
    if n==0:
        return [[1]]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal():
    """Tests pascal_rows"""
    assert pascal_row(0)==[1]
    assert pascal_row(1)==[1,1]
    assert pascal_row(5)==[1, 5, 10, 10, 5, 1]
    assert pascal_row(10)==[1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]

def test_pascal_triangle():
    """Tests pascal_triangle"""
    assert pascal_triangle(0)==[[1]]
    assert pascal_triangle(1)==[[1], [1, 1]]
    assert pascal_triangle(2)==[[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(5)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    
