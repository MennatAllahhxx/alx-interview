#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

from typing import List

def rotate_2d_matrix(matrix: List[List[int]]) ->  List[List[int]]:
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix
