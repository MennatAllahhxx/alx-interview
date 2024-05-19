#!/usr/bin/python3
"""
prime game module
"""


def isWinner(x, nums):
    """AI is creating summary for isWinner

    Args:
        x (int): the rounds
        nums (List[int]): list of int

    Returns:
        str: the winner
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)

    prime = [True] * (max_n + 1)
    prime[0] = prime[1] = False

    for start in range(2, int(max_n**0.5) + 1):
        if prime[start]:
            for multiple in range(start * start, max_n + 1, start):
                prime[multiple] = False

    primes_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
