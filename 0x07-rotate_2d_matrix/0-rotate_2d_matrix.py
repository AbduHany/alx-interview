#!/usr/bin/python3
""" This module rotates a 2D matrix
"""


def rotate_2d_matrix(matrix):
    """ This function rotates a 2D matrix
    in clockwise direction.
    Args:
        matrix (list): the matrix to rotate
    Returns:
        None
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
