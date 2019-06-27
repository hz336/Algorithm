"""
Given an array of integers, find how many pairs in the array such that their sum is bigger than a specific target number. Please return the number of
pairs.


Example
Given numbers = [2, 7, 11, 15], target = 24. Return 1. (11 + 15 is the only pair)
"""


class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """

    def twoSum2(self, nums, target):
        # write your code here
        if nums is None or len(nums) < 2:
            return 0

        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                left += 1
            else:
                count += right - left
                right -= 1

        return count