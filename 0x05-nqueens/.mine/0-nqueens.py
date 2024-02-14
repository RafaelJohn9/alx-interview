#!/usr/bin/python3
"""
the nqueens problem
"""
import sys

def is_unique(coordinates, queens):
    """
    checks for the valid space for a queen
    """


def nqueens(N):
    """
    finds the max possile number of moves possible in a N X N
    table for N number of queens
    """
    if not int(N):
        print("N must be a number")
        sys.exit(1)

    if int(N) < 4:
        print("N must be at least 4")
        sys.exit(1)

    i = 0;

    while (i < N):
        solution = [[0, i]]
        for x in range(N):
            for y in range(N):
                if  is_unique([x, y], solution):
                    solution.append([x, y])

        len (solution) == N:
            print(solution)
        i += 1
