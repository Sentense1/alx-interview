#!/usr/bin/python3
"""
Module for male Change.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    # If the total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    remainder = total

    coins_count = 0

    coin_index = 0

    # Sort the list of coins in descending order
    sorted_coins_list = sorted(coins, reverse=True)

    # Get the length of the list of coins
    list_len = len(coins)

    # Iterate until the remainder is reduced to 0
    while remainder > 0:
        # If we have considered all coin denominations
        #   and still have a non-zero remainder, it's not possible
        if coin_index >= list_len:
            return -1
        # If the current coin can be subtracted from the remainder,
        # update the counts
        if remainder - sorted_coins_list[coin_index] >= 0:
            remainder -= sorted_coins_list[coin_index]
            coins_count += 1
        else:
            # Move to the next coin denomination
            coin_index += 1
    # Return the total number of coins needed
    return coins_count


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
