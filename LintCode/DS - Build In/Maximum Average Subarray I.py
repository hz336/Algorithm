"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output
the maximum average value.

Notice
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

Example
Given nums = [1,12,-5,-6,50,3], k = 4, return 12.75.

Explanation:
Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
"""

import math


class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """

    def findMaxAverage(self, nums, k):
        # Write your code here
        if nums is None or len(nums) == 0:
            return -1

        max_sum = -math.inf
        total = [0]
        for i in range(len(nums)):
            total.append(total[i] + nums[i])
            if i >= k - 1:
                max_sum = max(max_sum, (total[i + 1] - total[i + 1 - k]) / k)

        return max_sum
