"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i]
+ nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""


class Solution:
    def threeSumSmaller(self, nums: 'List[int]', target: 'int') -> 'int':
        if nums is None or len(nums) < 3:
            return 0

        nums.sort()
        count = 0
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count

