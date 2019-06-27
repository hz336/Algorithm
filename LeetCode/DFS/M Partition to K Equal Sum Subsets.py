"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all
equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
"""

"""
Time Complexity: O(exponential)
Space Complexity: O(n)
"""


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if nums is None or len(nums) == 0 or k <= 0:
            return False

        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False

        visited = [False for _ in range(len(nums))]
        return self.dfs(nums, visited, 0, k, 0, 0, nums_sum // k)

    def dfs(self, nums, visited, index_start, k, cur_sum, cur_num, target):
        if k == 1:
            return True

        if cur_sum == target and cur_num > 0:
            return self.dfs(nums, visited, 0, k - 1, 0, 0, target)

        for i in range(index_start, len(nums)):
            if visited[i] == 0:
                visited[i] = 1
                if self.dfs(nums, visited, i + 1, k, cur_sum + nums[i], cur_num + 1, target):
                    return True
                visited[i] = 0

        return False
