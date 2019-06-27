"""
Given two rectangles, find if the given two rectangles overlap or not.

Notice
l1: Top Left coordinate of first rectangle.
r1: Bottom Right coordinate of first rectangle.
l2: Top Left coordinate of second rectangle.
r2: Bottom Right coordinate of second rectangle.

l1 != r2 and l2 != r2
"""


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param: l1: top-left coordinate of first rectangle
    @param: r1: bottom-right coordinate of first rectangle
    @param: l2: top-left coordinate of second rectangle
    @param: r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """

    def doOverlap(self, l1, r1, l2, r2):
        # write your code here
        if r1.x < l2.x or r2.x < l1.x:
            return False

        if l2.y < r1.y or l1.y < r2.y:
            return False

        return True

