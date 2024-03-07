#!/usr/bin/python3
"""
gets the perimeter of a grid
"""

def island_perimeter(grid):
    """
    grid is a 2 x 2 matrix
    """
    top = lambda co_ord: [co_ord[0] - 1, co_ord[1]]
    down = lambda co_ord: [co_ord[0] + 1, co_ord[1]]
    left = lambda co_ord: [co_ord[0], co_ord[1] - 1]
    right = lambda co_ord: [co_ord[0], co_ord[1] + 1]

    visited = []
    islandCoordinate = []

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                islandCoordinate = [x, y]
                break;

    nextCoordinates = []
    perimeter = 0

    while islandCoordinate not in visited:
        visited.append(islandCoordinate)
        determiner = [
                      top(islandCoordinate),
                      down(islandCoordinate),
                      left(islandCoordinate),
                      right(islandCoordinate)
                      ]
        for coordinate in determiner:
            if coordinate not in visited:
                x, y = coordinate

                if x < 0 or y >= len(grid[0]) or x >= len(grid):
                    perimeter += 1
                    continue

                if grid[x][y] == 1:
                    nextCoordinates.append([x, y])
                else:
                    perimeter += 1
        if len(nextCoordinates) > 0:
            islandCoordinate = nextCoordinates.pop()
    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
