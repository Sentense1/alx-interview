#!/usr/bin/python3
"""
Finds the minimum number of operations needed to obtain 'n' 'H' characters.
"""


def minOperations(n):
    """
    Finds the minimum number of operations needed to obtain 'n' 'H' characters.

    Args:
        n (int): The desired number of 'H' characters in the file.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    # Initialize a list to store the minimum operations for each i (0 to n).
    min_list = [0] * (n + 1)

    for i in range(2, n + 1):
        # Initialize to the worst case: copy all H and then paste.
        min_list[i] = i

        # Try all possible factors to see if we can optimize the process.
        for j in range(2, i):
            if i % j == 0:
                min_list[i] = min(min_list[i], min_list[j] + i // j)

    return min_list[n]



if __name__ == '__main__':
    n = 4
    print("Min # of ops to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of ops to reach {} char: {}".format(n, minOperations(n)))
