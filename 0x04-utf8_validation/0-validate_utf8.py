#!/usr/bin/python3
"""
Module contains validUTF8 fun
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """AI is creating summary for validUTF8

    Args:
        data (List[int]): data set to be checked

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """
    bytes_num = len(data)
    if bytes_num == 0:
        return True

    i = 0

    while i < bytes_num:
        ones_num = 0
        if (data[i] >> 7) & 1:
            ones_num = get_ones(data[i])
            if ones_num == 0:
                return False
            
            for j in range(ones_num):
                if (j + i + 2) > bytes_num or\
                   (((data[i + j + 1] >> 7) & 1) == 0) or\
                   (((data[i + j + 1] >> 6) & 1) == 1):
                    return False
        i += ones_num + 1
    return True


def get_ones(number: int) -> int:
    """AI is creating summary for get_ones

    Args:
        number (int): number to be checked

    Returns:
        int: number of ones
    """
    num = 0

    while number & (1 << 7):
        num += 1
        number = number << 1

    return num - 1
