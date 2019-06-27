"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the
candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""




class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
            self.dfs(nums, target - nums[i], i, subset, results)   # 可以重复选择，所以i不加1 
            subset.pop()

