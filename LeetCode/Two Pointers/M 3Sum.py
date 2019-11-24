"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the
sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        if nums is None or len(nums) < 3:
            return []

        results = []
        nums.sort()
        for i in range(len(nums)):
            if 0 < i < len(nums) - 1 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                if left < right and nums[i] + nums[left] + nums[right] < 0:
                    left += 1

                elif left < right and nums[i] + nums[left] + nums[right] > 0:
                    right -= 1

                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return results
