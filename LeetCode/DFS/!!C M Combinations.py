"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n or n <= 0 or k <= 0:
            return []

        subset = []
        results = []
        self.dfs(n, k, 1, subset, results)
        return results

    def dfs(self, n, k, index, subset, results):
        if len(subset) == k:
            results.append(subset.copy())

        for i in range(index, n + 1):
            subset.append(i)
            self.dfs(n, k, i + 1, subset, results)
            subset.pop()


