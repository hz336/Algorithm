"""
Given an array of integers, find a contiguous subarray which has the largest sum.

Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""

import math


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        max_sum = -math.inf
        min_sum = 0
        total = 0

        for num in nums:
            total += num
            max_sum = max(total - min_sum, max_sum)
            min_sum = min(total, min_sum)

        return max_sum








