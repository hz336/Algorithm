"""
Given an array of integers, find the subarray with smallest sum.

Return the sum of the subarray.

Notice
The subarray should contain one integer at least.

Example
For [1, -1, -2, 1], return -3.
"""

import math


class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

    def minSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        min_sum = math.inf
        max_sum = 0
        total = 0

        for num in nums:
            total += num
            min_sum = min(min_sum, total - max_sum)
            max_sum = max(max_sum, total)

        return min_sum
