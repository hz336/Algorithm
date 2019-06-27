"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example
For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6.
"""

import math


"""
Time Complexity: O(n)
Space Complexity: O(2n)
"""
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """

    def maxProduct(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return

        n = len(nums)
        f_max = [-math.inf] * n
        f_min = [math.inf] * n

        for index, value in enumerate(nums):
            if index == 0:
                f_max[index] = f_min[index] = value
                continue

            f_max[index] = max(value, value * f_max[index - 1], value * f_min[index - 1])
            f_min[index] = min(value, value * f_max[index - 1], value * f_min[index - 1])

        return max(f_max)

