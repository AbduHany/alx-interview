#!/usr/bin/python3
""" This module defines the makeChange function
"""
import sys


def makeChange(coins, total):
    """ This function calculates the fewest number of coins
    needed to meet a given amount total
    Args:
        coins: list of the values of the coins
        total: amount
    Returns:
        fewest number of coins needed to meet total
    """
    coins.sort(reverse=True)  # Sort coins in descending order
    ans = 0  # To keep track of the number of coins used

    for coin in coins:
        if total == 0:
            break  # Stop if the total is met
        if coin <= total:
            num_coins = total // coin  # Find how many of this coin can be used
            ans += num_coins
            total -= num_coins * coin  # Reduce the total by the coin value

    # If we still have a total left, it's not possible to make that total
    if total != 0:
        return -1

    return ans
    # table = [0 for i in range(total + 1)]
    # table[0] = 0
    # # initializing the table with infinite values
    # for i in range(1, total + 1):
    #     table[i] = sys.maxsize
    # # compute minimum coins required
    # for i in range(1, total + 1):
    #     # go through smaller coins solutions
    #     for j in range(n):
    #         if (coins[j] <= i):
    #             sub_res = table[i - coins[j]]
    #             if sub_res != sys.maxsize and sub_res + 1 < table[i]:
    #                 table[i] = sub_res + 1
    # if table[total] == sys.maxsize:
    #     return -1
    # return table[total]
