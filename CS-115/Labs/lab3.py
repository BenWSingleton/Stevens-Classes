from cs115 import *

def change(amount, coins):
    """Returns a non-negative integer indicating the minimum
    number of coins required to make up the given amount"""
    if amount==0:
        return 0
    elif coins==[] or amount < 0:
        return float("inf")
    elif coins[0]>amount:
        return change(amount, coins[1:])
    else:
        use=change(amount-coins[0], coins)+1
        lose=change(amount, coins[1:])
    return min(use, lose)
