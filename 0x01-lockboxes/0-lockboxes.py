#!/usr/bin/python3
"""
the lockbox problem
You have n number of locked boxes in front of you.

Each box is numbered sequentially from 0 to n - 1 and
    each box may contain keys to the other boxes.:11

Write a method that determines if all the boxes can be opened.
first box is always unlocked
"""


def canUnlockAll(boxes):
    """
    the function that solves the problem
    """
    # populate the required amount of locked boxes
    lockedBoxes = {}
    for i in range(len(boxes)):
        lockedBoxes[i] = 0

    # first box is unlocked
    lockedBoxes[0] = 1

    # open the boxes that can be opened
    for box in boxes:
        for key in box:
            if key == boxes.index(box):
                continue
            if key < len(boxes):
                lockedBoxes[key] = 1

    # check if there is any locked boxes
    for box in lockedBoxes.keys():
        if lockedBoxes[box] == 0:
            return False
    return True
