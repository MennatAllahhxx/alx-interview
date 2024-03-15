#!/usr/bin/python3
"""
Module contains canUnlockAll and boxUnlocked funs
"""


def canUnlockAll(boxes):
    """AI is creating summary for canUnlockAll

    Args:
        boxes (List[List[int]]): a list of lists

    Returns:
        bool: True if all boxes can be opened, else return False
    """
    num_of_boxes = len(boxes)
    checklist = [0 for box in range(num_of_boxes)]
    checklist[0] = 1

    checklist_updated = boxUnlocked(boxes, boxes[0], checklist)

    for check in checklist_updated:
        if (check == 0):
            return False
    return True


def boxUnlocked(boxes, keys_inside, checklist):
    """AI is creating summary for boxUnlocked

    Args:
        boxes (List[List[int]]): a list of lists
        keys_inside (List[int]): a list of keys
        checklist (List): a list of int

    Returns:
        Checklist: returns checklist after update
    """
    for key_inside in keys_inside:
        if (checklist[key_inside]):
            return checklist

        checklist[key_inside] = 1
        boxUnlocked(boxes, boxes[key_inside], checklist)
    return checklist
