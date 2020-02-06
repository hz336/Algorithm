"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

""" 
Time complexity: O(n * n!) 
It takes O(n) time to construct 1 permutation, and there are O(n!) permutations in total. 
DFS
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False] * len(nums)
        subset = []
        results = []
        self.dfs(nums, visited, subset, results)
        return results

    def dfs(self, nums, visited, subset, results):
        if len(subset) == len(nums):
            results.append(subset.copy())

        for i in range(len(nums)):
            if visited[i]:
                continue

            if i != 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            subset.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, subset, results)
            subset.pop()
            visited[i] = False

