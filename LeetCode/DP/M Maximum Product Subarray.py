"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

"""
Time Complexity: O(n)
Space Complexity: O(2n)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f_max = [float('-inf')] * len(nums)
        f_min = [float('inf')] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                f_max[i] = f_min[i] = nums[i]
                continue

            f_max[i] = max(nums[i], max(nums[i] * f_max[i - 1], nums[i] * f_min[i - 1]))
            f_min[i] = min(nums[i], min(nums[i] * f_max[i - 1], nums[i] * f_min[i - 1]))

        return max(f_max)



