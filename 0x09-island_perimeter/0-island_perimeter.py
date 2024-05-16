#!/usr/bin/python3
"""
island perimeter calculator
"""
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """AI is creating summary for island_perimeter

    Args:
        grid (List[List[int]]): island

    Returns:
        int: perimeter
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 2

                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 2

    return perimeter
