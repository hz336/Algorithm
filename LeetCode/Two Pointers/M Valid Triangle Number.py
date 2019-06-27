"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we
take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3

Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""


class Solution:
    def triangleNumber(self, nums: 'List[int]') -> 'int':
        if nums is None or len(nums) < 3:
            return 0

        nums.sort()
        count = 0
        for i in range(2, len(nums)):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count



