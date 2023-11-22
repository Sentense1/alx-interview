#!/usr/bin/python3
"""
Minimum/fewer operation to meet a given total
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    # Initialize a list to store the minimum number
    #   of coins needed for each amount
    min_list = [float('inf')] * (total + 1)

    # Base case: To make a total of 0, no coins are needed
    min_list[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            # Update the minimum number of coins needed for the current amount
            min_list[i] = min(min_list[i], min_list[i - coin] + 1)

    # If it's not possible to make the total
    #   amount with the given coins, return -1
    if min_list[total] == float('inf'):
        return -1
    else:
        # Otherwise, return the minimum number of coins needed
        #   for the total amount
        return min_list[total]


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
