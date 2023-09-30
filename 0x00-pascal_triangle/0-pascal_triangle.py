#!/usr/bin/python3
# Returns a list of lists of integers representing Pascal's triangle of n

def pascal_triangle(n):
    """Representing Pascal's triangle.

    Args:
        n - Size of the triangle.

    Returns:
        List of lists of integers.
    """
    # Check if n is less than or equal to 0, return an empty list in such cases
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    pas_triangle = [[1]]

    for i in range(1, n):
        # Calculate the next row using the previous row
        # Get the last row of the triangle
        prev_row = pas_triangle[-1]
        # Initialize the new row with 1 (the first element)
        new_row = [1]

        for j in range(1, i):
            # Calculate the middle elements of the new row
            new_row.append(prev_row[j - 1] + prev_row[j])

        # Add 1 to the end of the new row
        new_row.append(1)
        # Add the new row to the triangle
        pas_triangle.append(new_row)

    return pas_triangle
