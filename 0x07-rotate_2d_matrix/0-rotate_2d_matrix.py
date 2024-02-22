#!/usr/bin/python3

"""
rotates a 2d matrix by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    matrix- a n x n matrix
    must be edited in-place
    assumption= the matrix will have 2 x 2 dimension and will
    not be empty
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)
