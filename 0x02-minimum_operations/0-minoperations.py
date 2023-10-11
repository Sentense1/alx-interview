#!/usr/bin/python3
"""
Minimum Operations's Modules
"""


def minOperations(n):
    """
    Finding minimum operation of n of H characater.
    """

    if n <= 1:
        return 0
    num, div, numOfOperations = n, 2, 0

    while num > 1:
        if num % div == 0:
            num = num / div
            numOfOperations = numOfOperations + div
        else:
            div += 1
    return numOfOperations


if __name__ == '__main__':
    n = 4
    print("Min # of ops to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of ops to reach {} char: {}".format(n, minOperations(n)))
