"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        if nums is None or len(nums) == 0:
            return None

        m = {}
        for i in range(len(nums)):
            if target - nums[i] in m:
                return [m[target - nums[i]], i]

            m[nums[i]] = i

        return None


"""
Follow up: Can you solve it with O(1) space complexity?
Then it becomes question 'E Two Sum II - Input array is sorted'
"""



