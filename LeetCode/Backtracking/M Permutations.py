"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

""" 
Time complexity: O(n * n!) 
It takes O(n) time to construct 1 permutation, and there are O(n!) permutations in total. 
DFS
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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

            subset.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, subset, results)
            subset.pop()
            visited[i] = False

