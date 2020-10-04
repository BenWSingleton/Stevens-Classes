#Benjamin Singleton
#I pledge my honor that I have abided by the Stevens Honor System

from cs115 import *

def knapsack(capacity, itemList):
    if capacity==0 or itemList==[]:
        return [0, []]
    elif (itemList[0][0])>capacity:
        return knapsack(capacity, itemList[1:])
    else:
        [lose, loseList]=knapsack(capacity, itemList[1:])
        [use, useList]=knapsack(capacity-itemList[0][0], itemList[1:])
        useList=[itemList[0]]+useList
        use=use+itemList[0][1]
        if use < lose:
            return [lose, loseList]
        else:
            return [use, useList]
