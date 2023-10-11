#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    """
    Unlock boxes that can be opened.

    Args:
        boxes - boxes to unlock

    Returns:
        True if all boxes can be opened, else return False
    """
    n = len(boxes)  # Total number of boxes.
    seen_boxes = set([0])  # Set to keep track of seen boxes (starting with box 0).
    
    # Initialize a set of unseen boxes, which starts with the keys from box 0.
    unseen_boxes = set(boxes[0]).difference(set([0]))

    # Continue until there are unseen boxes to explore.
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()  # Get the next unseen box index.

        # Check if the box index is out of bounds, if so, skip it.
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue

        # If the box has not been seen yet, add its keys to the set of unseen boxes.
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)

    # Check if all boxes have been seen during traversal.
    return n == len(seen_boxes)


if __name__ == '__main__':
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
