"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the
three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""


class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        if nums is None or len(nums) < 3:
            return 0

        import math
        min_diff = math.inf
        result = None

        nums.sort()
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                diff = abs(nums[i] + nums[left] + nums[right] - target)
                if diff < min_diff:
                    result = nums[i] + nums[left] + nums[right]
                    min_diff = diff

                if left < right and nums[i] + nums[left] + nums[right] < target:
                    left += 1
                elif left < right and nums[i] + nums[left] + nums[right] > target:
                    right -= 1
                else:
                    return target

        return result
