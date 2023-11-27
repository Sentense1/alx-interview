#!/usr/bin/python3
"""
Module for finding the perimeter of an island
"""


def island_perimeter(grid):
    """
    Returns the perimeter of an island.
    Where grid is the body of both water(0) and land(1)
    """
    # initialise perimeter to keep track of the size of island
    perimeter = 0

    # initialize the length of grid
    grid_row = len(grid)

    # initialize the width of grid
    grid_column = len(grid[0])

    # iterate through the grid_row
    for i in range(grid_row):
        # iterate through the grid_column
        for j in range(grid_column):
            # check for 1s as they represent lands
            if grid[i][j] == 1:
                # add 4 to perimeter as each land is a square
                perimeter += 4

                # check for land above eache cell block and remove the
                # 1 for the shared side
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < grid_row - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < grid_column - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1
    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
