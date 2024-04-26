#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """AI is creating summary for rotate_2d_matrix

    Args:
        matrix (List[List[int]]): matrix to be reversed

    Returns:
        List[List[int]]: reversed matrix
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()