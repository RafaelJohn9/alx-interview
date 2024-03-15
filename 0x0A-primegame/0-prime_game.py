#!/usr/bin/python3
"""
a prime game
winner is the one whogets the final prime number
"""


def sieveOfEratosthenes(n):
    """
    gets all the prime numbers in a certain range
    and returns it in a list
    """
    if n <= 1:
        return []

    # gets all the numbers in range n
    allNumbersInRange = [num for num in range(2, n + 1)]

    # variables that will be used during the iteration
    i = 0
    factor = 2  # factors  of the number being sieved
    number = allNumbersInRange[i]   # the number being sieved of its multiples
    resultingNumber = factor * number # the resulting multiples

    while i < len(allNumbersInRange):
        if resultingNumber <= n:
            # try block is used to make sure if a number is repeated its ignored
            try:
                index = allNumbersInRange.index(resultingNumber)
            except ValueError:
                factor += 1
                resultingNumber = factor * number
                continue

            del(allNumbersInRange[index])

            factor += 1
            resultingNumber = factor * number
            continue

        factor = 2
        i += 1
        if i >= len(allNumbersInRange):
                break
        number = allNumbersInRange[i]
        resultingNumber =  factor * number

    return allNumbersInRange


def isWinner(x, nums):
    """
    determines the winner in the prime game
    @x -> is the number of rounds
    @nums -> a list that contains the ranges of n in an instance
    """
    gamesWon = {
                  "Maria": 0,
                  "Ben" : 0
                  }
    winner = lambda x: "Ben" if len(x) % 2 == 0 else "Maria"

    for num in nums:
        allPrimes = sieveOfEratosthenes(num)
        if len(allPrimes) < (x * 2):
            gamesWon[winner(allPrimes)] += 1
        else:
            gamesWon['Ben'] += 1

    return "Winner: Maria" if gamesWon["Maria"] > gamesWon["Ben"] else "Winner: Ben"


if __name__=="__main__":
    print(isWinner(2, [2, 5, 6, 8]))
