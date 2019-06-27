"""
Given a continuous stream of numbers, write a function that returns the first unique number whenever terminating number is reached(include terminating number). If there no unique number before terminating number or you can't find this terminating number, return -1.

Example
Given a stream [1, 2, 2, 1, 3, 4, 4, 5, 6] and a number 5
return 3

Given a stream [1, 2, 2, 1, 3, 4, 4, 5, 6] and a number 7
return -1
"""


class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """

    def firstUniqueNumber(self, nums, number):
        # Write your code here
        if nums is None or len(nums) == 0:
            return -1

        mapping = {}
        for index, value in enumerate(nums):
            if value not in mapping:
                mapping[value] = True
            else:
                mapping[value] = False

            if value == number:
                break

        if number not in mapping:
            return -1

        for index, value in enumerate(nums):
            if value == number:
                break

            if mapping[value] is True:
                return value

        return -1


