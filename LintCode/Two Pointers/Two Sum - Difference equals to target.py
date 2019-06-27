"""
Given an array of integers, find two numbers that their difference equals to a target value.
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

Example
Given nums = [2, 7, 15, 24], target = 5
return [1, 2] (7 - 2 = 5)
"""

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    # version 1. Hashmap - O(n) time complexity, O(n) space complexity
    # Hashmap is easier because array is sorted and the return value is index
    def twoSum7_v1(self, nums, target):
        if nums is None or len(nums) < 2:
            return None

        mapping = {}
        for i, v in enumerate(nums):
            if v in mapping:
                return [mapping[v] + 1, i + 1]

            mapping[v + target] = i
            mapping[v - target] = i

    # version 2. Two Pointers O(nlogn) time compelxity, O(1) space compelxity
    def twoSum7(self, nums, target):
        # write your code here
        if nums is None or len(nums) < 2:
            return []

        nums_sort = sorted(nums)
        target = abs(target)
        left, right = 0, 1
        while left < len(nums_sort) - 1 and right < len(nums_sort):
            while left + 1 < right and nums_sort[right] - nums_sort[left] > target:
                left += 1

            if nums_sort[right] - nums_sort[left] == target:
                break

            right += 1

        for i in range(len(nums)):
            if nums[i] == nums_sort[right]:
                break

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == nums_sort[left]:
                break

        return sorted([i + 1, j + 1])
