#!/usr/bin/env/ python3
"""
Module for utf-8 validation
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Validates data for utf-8
    """
    # Initialize a variable to keep track of the number of continuation bytes
    num_continuation_bytes = 0

    # Iterate through the list of integers (each representing 1 byte of data).
    for byte in data:
        # Check if the byte is a continuation byte (starts with '10' in binary)
        if num_continuation_bytes > 0:
            if bin(byte)[2:4] != '10':
                return False
            num_continuation_bytes -= 1
        else:
            # Determine the number of continuation bytes for the current char
            if bin(byte)[2:4] == '11':
                num_continuation_bytes = 1
            elif bin(byte)[2:5] == '111':
                num_continuation_bytes = 2
            elif bin(byte)[2:6] == '1111':
                num_continuation_bytes = 3
            elif bin(byte)[2] == '0':
                num_continuation_bytes = 0
            else:
                return False

    # If there are unmatched continuation bytes, return False.
    return num_continuation_bytes == 0

if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]  # noqa
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
