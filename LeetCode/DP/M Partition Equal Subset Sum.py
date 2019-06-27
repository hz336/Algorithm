"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in
both subsets is equal.


Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

"""
可行性型DP
Time Complexity: O(length of array * sum of the array / 2)
Space Complexity: O(length of array * sum of the array / 2)
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False

        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False

        target = nums_sum // 2
        f = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            f[i][0] = True

        for j in range(1, target + 1):
            f[0][j] = False

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                f[i][j] = f[i - 1][j]
                if j >= nums[i - 1]:
                    f[i][j] = (f[i][j] or f[i - 1][j - nums[i - 1]])

        return f[len(nums)][target]

