#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [0], [3], [4], []]
print(canUnlockAll(boxes))

