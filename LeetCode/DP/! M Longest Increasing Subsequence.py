"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

"""
Dynamic Programming
Time Complexity: O(n^2)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        length = len(nums)
        f = [1] * length
        for curr in range(length):
            for prev in range(curr):
                if nums[prev] < nums[curr]:
                    f[curr] = max(f[curr], f[prev] + 1)

        return max(f)


