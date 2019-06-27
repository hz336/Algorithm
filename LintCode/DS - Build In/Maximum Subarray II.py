"""
Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

Notice
The subarray should contain at least one number

Example
For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2], they both have the largest sum 7.
"""

import math


class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        left = [0] * len(nums)
        right = [0] * len(nums)

        max_sum = -math.inf
        min_sum = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            max_sum = max(max_sum, total - min_sum)
            min_sum = min(min_sum, total)
            left[i] = max_sum

        max_sum = -math.inf
        min_sum = 0
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            total += nums[i]
            max_sum = max(max_sum, total - min_sum)
            min_sum = min(min_sum, total)
            right[i] = max_sum

        max_sum = -math.inf
        for i in range(len(nums) - 1):
            max_sum = max(max_sum, left[i] + right[i + 1])

        return max_sum


