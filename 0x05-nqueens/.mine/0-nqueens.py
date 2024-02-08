#!/usr/bin/python3
"""
the nqueens problem
"""
import sys


def nqueens(N):
    if not int(N):
        print("N must be a number")
        sys.exit(1)

    if int(N) < 4:
        print("N must be at least 4")
        sys.exit(1)

    i = 0;

    solutions = []
    for row, column in zip(range(N), range(N)):
        coordinates = [row, column]
        if is_unique(coordinates):
            solutions.append(coordinates)
    print(solutions)
