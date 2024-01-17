#!/usr/bin/python3
"""
python function that solves minimum operations
"""


def minOperations(n):
    """
    a text file there is a single char H your
    text editor can execute only two operations in this file copy All and Paste
    give the min num of operations to achieve n times of H
    """
    if n <= 0:
        return 0

    numberOfOperations = 0
    numberOfPastes = 0
    string = "H"
    toBeCopied = string

    while len(string) < n:
        if numberOfPastes < 2:
            string += toBeCopied
            numberOfPastes += 1
            numberOfOperations += 1
        else:
            numberOfPastes = 0
            toBeCopied = string
            numberOfOperations += 1

    return numberOfOperations
