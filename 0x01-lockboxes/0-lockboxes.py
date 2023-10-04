#!/usr/bin/python3
# Determines if all the boxes can be opened.
#    Each box may contain keys to the other boxes.

""" Method that determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    """
    Unlock boxes that can be opened.

    Args:
        boxes - boxes to unlock

    Returns:
        True if all boxes can be opened, else return False
    """
    # Total number of boxes in the input.
    n = len(boxes)

    # Use set to keep track of seen boxes during transversal.
    seen_boxes = set()

    # List to store the box numbers with keys.
    # We start with the first box (box 0) which is unlocked
    box_with_keys = [0]

    # Loop through boxes with keys
    while box_with_keys:
        # Get the latest box with keys to explore
        current_box = box_with_keys.pop()

        # Mark the current box as seen by adding to seen_boxes
        seen_boxes.add(current_box)

        # Check the keys in the current box and
        #   add unvisited box numbers to the list of keys.
        for key in boxes[current_box]:
            if key not in seen_boxes:
                # Add unvisited box numbers to the list of keys to explore.
                box_with_keys.append(key)

    # If all boxes have been seen, return True; otherwise, return False
    return len(seen_boxes) == n

