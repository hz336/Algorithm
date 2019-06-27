"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

"""
Time Complexity: O(n^3)
Space Complexity: O(n)
"""


class Solution:
    def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        if nums is None or len(nums) < 4:
            return []

        results = []
        nums.sort()

        for i in range(len(nums)):
            if 0 < i < len(nums) and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if i + 1 < j < len(nums) and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, len(nums) - 1
                while left < right:
                    if left < right and nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif left < right and nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return results


