#!/usr/bin/python3
"""
module that contains the pascal triangle function
"""


def pascal_triangle(n):
    """
    pascals triangle function
    """
    if n <= 0:
        emptyList = []
        return(emptyList)
    i = 0
    pascalsList = []

    previousList = []
    while i < n:
        currentList = []
        currentList.append(1)
        if i == 0:
            pascalsList.append(currentList)
            previousList == currentList
            i += 1
            continue
        elif i == 1:
            currentList.append(1)
            pascalsList.append(currentList)
            previousList = currentList
            i += 1
            continue
        else:
            index = 0
            while index + 1 < len(previousList):
                operation = previousList[index] + previousList[index + 1]
                currentList.append(operation)
                index += 1
            currentList.append(1)
            pascalsList.append(currentList)
            previousList = currentList
            index += 1
        i += 1
    return pascalsList
