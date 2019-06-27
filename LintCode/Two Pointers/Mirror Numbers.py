"""
A mirror number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is mirror. The number is represented as a string.

Example
For example, the numbers "69", "88", and "818" are all mirror numbers.
Given num = "69" return true
Given num = "68" return false
"""


class Solution:
    """
    @param: num: a string
    @return: true if a number is strobogrammatic or false
    """

    def isStrobogrammatic(self, num):
        # write your code here
        mirror = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        left = 0
        right = len(num) - 1
        while left <= right:
            if mirror.get(num[left]) != num[right]:
                return False

            left += 1
            right -= 1

        return True