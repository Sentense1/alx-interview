#!/usr/bin/python3
"""
Module to validate UTF-8 encoding
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Validates whether the given data represents valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers, each representing 1 byte of data.

    Returns:
        bool: True if data is valid UTF-8 encoding, False otherwise.
    """
    num_continuation_bytes = 0

    for byte in data:
        # Ensure each byte has 8 bits in binary representation
        binary_byte = bin(byte)[2:].rjust(8, '0')

        if num_continuation_bytes > 0:
            if not binary_byte.startswith('10'):
                return False
            num_continuation_bytes -= 1
        else:
            if binary_byte.startswith('0'):
                num_continuation_bytes = 0
            elif binary_byte.startswith('110'):
                num_continuation_bytes = 1
            elif binary_byte.startswith('1110'):
                num_continuation_bytes = 2
            elif binary_byte.startswith('11110'):
                num_continuation_bytes = 3
            else:
                return False

    return num_continuation_bytes == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]  # noqa
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
