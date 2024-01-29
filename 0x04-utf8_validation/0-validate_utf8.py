#!/usr/bin/python3
"""
a method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    validates UTF8
    """
    for num in data:
        if len(bin(num)[2:]) < 9:
            continue
        else:
            return False
    return True
