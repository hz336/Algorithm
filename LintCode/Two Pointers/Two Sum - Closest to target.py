"""
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the difference between the sum of the two integers and the target.

Example
Given array nums = [-1, 2, 1, -4], and target = 4.

The minimum difference is 1. (4 - (2 + 1) = 1).
"""

import math


class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return

        nums.sort()
        min_diff = math.inf
        left, right = 0, len(nums) - 1
        while left < right:
            diff = nums[left] + nums[right] - target
            min_diff = min(abs(diff), abs(min_diff))

            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return 0

        return min_diff

