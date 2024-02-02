#!/usr/bin/python3
"""module for the function validUTF8"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Returns True if a given data set represents a valid UTF-8 encoding."""
    count = 0
    for s in data:
        binny = bin(s)[2:].zfill(8)[-8:]
        if binny.startswith("0") and count == 0:
            continue
        if binny.startswith("110") and count == 0:
            count = 1
            continue
        if binny.startswith("1110") and count == 0:
            count = 2
            continue
        if binny.startswith("11110") and count == 0:
            count = 3
            continue
        if binny.startswith("10") and count > 0:
            count -= 1
            continue
        return False
    return count == 0
