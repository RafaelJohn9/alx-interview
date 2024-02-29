#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins
needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    solution to the makeChange problem
    """
    coins.sort()
    coins.reverse()
    fewestNumberOfCoins = 0
    
    for coin in coins:
        coinDenomination = total // coin
        fewestNumberOfCoins += coinDenomination
        total -= coin * coinDenomination
    if total:
        return -1
    return fewestNumberOfCoins
