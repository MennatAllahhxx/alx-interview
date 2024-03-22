#!/usr/bin/python3
"""
Module contains minOperations fun
"""


def minOperations(n: int) -> int:
    """AI is creating summary for minOperations

    Args:
        n (int): the factor to print H times

    Returns:
        int: least number of operations.
    """
    ops: int = 1
    copy_value = 1
    items: int = 0
    left: int = n - items
    while left > 0:
        items = items + copy_value
        left = n - items
        if left == items:
            ops = ops + 2
            break
        if ((left % (3 * copy_value)) == 0) and (copy_value != 1):
            copy_value = items * 2
            ops = ops + 2
        elif left == 2 * items:
            ops = ops + 3
            break
        else:
            ops = ops + 1

    return ops
