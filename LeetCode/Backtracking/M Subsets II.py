"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

"""
Time Complexity: O(n * 2^n)
Space Complexity: O(2^n)
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []
        self.dfs(sorted(nums), 0, subset, results)
        return results

    def dfs(self, nums, index, subset, results):
        results.append(subset.copy())

        for i in range(index, len(nums)):
            # nums[i] == nums[i - 1]：  当前的数和前一个数相等
            # i > index：               当前的数不是第一个index， 比如nums=[1, 2, 2, 2], index在第二个2不continue, 在第三个2continue
            # i != 0:                   防止数组越界
            if i != index and nums[i] == nums[i - 1]:
                continue

            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            subset.pop()

