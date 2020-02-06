"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate
numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    def dfs(self, nums, target, index, subset, results):
        if target == 0:
            results.append(subset.copy())

        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue

            if target - nums[i] < 0:
                break

            subset.append(nums[i])
            self.dfs(nums, target - nums[i], i + 1, subset, results) # 不可以重复选择，所以i + 1
            subset.pop()
