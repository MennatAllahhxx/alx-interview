#!/usr/bin/python3
"""
Module contains makeChange func
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """AI is creating summary for makeChange

    Args:
        coins (List[int]): pile of coins
        total (int): to be met
    Returns:
        int: fewest number of coins needed
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    num_coins = 0
    remainder = total

    for coin in coins:
        while coin <= remainder:
            num_coins += 1
            remainder -= coin
    if remainder == 0:
        return num_coins
    else:
        return -1
