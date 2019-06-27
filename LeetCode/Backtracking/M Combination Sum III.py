"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be
a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        results = []
        self.dfs(nums, [], 0, k, n, results)
        return results

    def dfs(self, nums, subset, index, k, target, results):
        if len(subset) == k and target == 0:
            results.append(subset.copy())

        for i in range(index, len(nums)):
            if target < nums[i]:
                break

            subset.append(nums[i])
            self.dfs(nums, subset, i + 1, k, target - nums[i], results)
            subset.pop()



