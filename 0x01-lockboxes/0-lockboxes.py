#!/usr/bin/python3
"""Thid module defines the canUnlockAll function
"""


def canUnlockAll(boxes):
    """This function defines the solution for the lockboxes
    tech interview problem
    Args:
        boxes (List): List of Lists representing a box with each
        box containing keys.
    Returns:
        True - if all boxes can be unlocked
        False - if not all boxes can be unlocked
    """
    openedBoxes = [0]
    keys = []
    for key in boxes[0]:
        keys.append(key)

    while keys != []:
        key = keys.pop(0)
        openedBoxes.append(key)
        for newKey in boxes[key]:
            if newKey not in openedBoxes:
                keys.append(newKey)
    if (len(openedBoxes) == len(boxes)):
        return True
    return False
