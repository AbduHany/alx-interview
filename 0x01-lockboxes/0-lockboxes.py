#!/usr/bin/python3

def canUnlockAll(boxes):
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
