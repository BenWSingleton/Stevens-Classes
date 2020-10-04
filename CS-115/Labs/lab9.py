# mandelbrot.py
# Lab 9
#
# Name: Benjmain Singleton
# Date: 10/31/2019
# Pledge: I pledge my honor that I have abided by the Stevens Honor System

# keep this import line...
from cs5png import PNGImage
from cs115 import *

# start your Lab 9 functions here:
def mult(c,n):
    """mult uses only a loop and addition to multiply c by integer n"""
    result = 0
    for x in range( n ):
        result=result+c
    return result

def update(c,n):
    """Update starts with z=0 and runs z=z**2+c for a total of
    n times. It returns the final z."""
    z=0
    for x in range(n):
        z=z**2+c
    return z

def inMSet(c, n):
    """ inMSet takes in
            c for the update step of z = z**2+c
             n, the maximum number of times to run that step
         Then, it should return
             False as soon as abs(z) gets larger than 2
             True if abs(z) never gets larger than 2 (for n iterations)
 """
    z=0
    for x in range(n):
        z=z**2+c
        if abs(z)>2:
            return False
    return True

def weWantThisPixel(col,row):
    """a function that returns True if we want
       the pixel at col,row and False otherwise"""
    if col%10==0 and row%10==0:
        return True
    else:
        return False

def test():
    """a function to demonstrate how
       to create and save a png image"""
    width=300
    height=200
    image=PNGImage(width, height)
    #create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col,row)==True:
                image.plotPoint(col,row)
    #we looped through every image pixel; we now write the file
    image.saveFile()

#By changing the "and" in weWantThisPixel to "or" the test.png image becomes
#comprised of boxes instead of dotts.

def scale(pix, pixelMax, floatMin, floatMax):
    """scale takes in:
            pix, the CURRENT pixel column (or row)
            pixMax, the total # of pixel columns
            floatMin, the min floating-point value
            floatMax, the max floating-point value
        scale returns the floating-point value that
            corresponds to pix
    """
    return (1.0*pix / pixelMax)*(floatMax - floatMin) + floatMin

def mset():
    """creates a 300x200 image of the Mandlebrot set
    """
    width=300
    height=200
    image=PNGImage(width, height)
    
    #create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            x=scale(col, 300, -2.0, 1.0)
            y=scale(row, 200, -1.0, 1.0)
            c=(x)+(y*1j)
            if inMSet(c,n=25)==True:
                image.plotPoint(col,row)
    image.saveFile()
