"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Notice
You don't need to care the order of combinations, but you should make sure the numbers in a combination are sorted.

Example
Given n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4]
]
"""


class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """

    def combine(self, n, k):
        # write your code here
        results = []
        self.dfs(range(1, n + 1), k, 0, [], results)

        return results

    def dfs(self, nums, k, index, subset, results):
        if k == 0:
            results.append(subset.copy())

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, k - 1, i + 1, subset, results)
            subset.pop()

