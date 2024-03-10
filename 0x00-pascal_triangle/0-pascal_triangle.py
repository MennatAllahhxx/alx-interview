#!/usr/bin/python3y
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    a function that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if (n <= 0):
        return []

    output = [[0 for b in range(a + 1)] for a in range(n)]

    for i in range(n):
        if (i % 2 == 0):
            r = round((i+2)/2)
        else:
            r = round((i+1)/2)

        for j in range(r):
            if ((i - 1) >= 0):
                x = output[i - 1][j]
                if ((j - 1) >= 0):
                    y = output[i-1][j-1]
                else:
                    y = 0
            elif (i == 0):
                x = 1
                y = 0
            else:
                x = 0
            output[i][j] = x + y
            output[i][-1-j] = x + y
    return output


if __name__ == "__main__":
    pascal_triangle(n)
