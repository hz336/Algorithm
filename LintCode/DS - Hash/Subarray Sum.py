"""
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the
last number.

Notice
There is at least one subarray that it's sum equals to zero.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
"""


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []

        mapping = {0: -1}
        total = 0
        for key, value in enumerate(nums):
            total += value
            if total not in mapping:
                mapping[total] = key
            else:
                return [mapping[total] + 1, key]

        return []

