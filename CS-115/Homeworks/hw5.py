'''
Created on 10/06/2019
@author:   Benjamin Singleton
Pledge:    I pledge my honor that I hava abided by the Stevens Honor System.

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    if levels>0:
        turtle.forward(trunk_length)
        turtle.right(30)
        sv_tree(trunk_length//2, levels-1)
        turtle.left(60)
        sv_tree(trunk_length//2, levels-1)
        turtle.right(30)
        turtle.backward(trunk_length)


def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def fast_lucas_helper(n, memo):
        if n in memo:
            return memo[n]
        elif n==0:
            answer=2
        elif n==1:
            answer=1
        else:
            answer=fast_lucas_helper(n-1, memo)+fast_lucas_helper(n-2, memo)
        memo[n]=answer
        return answer
    return fast_lucas_helper(n, {})     

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        if amount==0:
            memo[(amount, coins)]=0
            return 0
        elif coins==() or amount < 0:
            answer=float("inf")
            memo[(amount, coins)]=answer
            return answer
        elif coins[0]>amount:
            answer=fast_change_helper(amount, coins[1:], memo)
            memo[(amount, coins)]=answer
            return answer
        else:
            use=fast_change_helper(amount-coins[0], coins, memo)+1
            lose=fast_change_helper(amount, coins[1:], memo)
            answer=min(use, lose)
            memo[(amount, coins)]=answer
            return answer
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
