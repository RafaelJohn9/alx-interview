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
    string = "H"
    copy = lambda src: src
    paste = lambda string1, string2: string1 + string2
    numberOfOperations = 0
    typeOfn = "odd" if n % 2 != 0 else "even"

    while len(string) < n:
        if n % len(string) == 0:
            strCopied = copy(string)
            string = paste(strCopied, string)
            numberOfOperations += 2

        else:
            string = paste(strCopied, string)
            numberOfOperations += 1

    return numberOfOperations
