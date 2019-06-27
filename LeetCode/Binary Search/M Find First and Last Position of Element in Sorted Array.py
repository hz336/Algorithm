"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

"""
Time Complexity: O(logn)
Space Complexity: O(1)
"""


class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        if nums is None or len(nums) == 0:
            return [-1, -1]

        # Find the first position
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            start_position = start
        elif nums[end] == target:
            start_position = end
        else:
            return [-1, -1]

        # Find the last position
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            last_position = end
        elif nums[start] == target:
            last_position = start
        else:
            return [-1, -1]

        return [start_position, last_position]
