"""
Given an integer arrays, find a contiguous subarray which has the largest sum and length should be greater or equal to given length k.
Return the largest sum, return 0 if there are fewer than k elements in the array.

Example
Given the array [-2,2,-3,4,-1,2,1,-5,3] and k = 5, the contiguous subarray [2,-3,4,-1,2,1] has the largest sum = 5.
"""

import math


class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """

    def maxSubarray4(self, nums, k):
        # write your code here
        if nums is None or len(nums) < k:
            return 0

        max_sum = -math.inf
        min_sum = 0
        total = [0]
        for i in range(1, len(nums) + 1):
            total.append(total[i - 1] + nums[i - 1])

            if i >= k:
                max_sum = max(max_sum, total[i] - min_sum)
                min_sum = min(min_sum, total[i - k + 1])

        return max_sum





