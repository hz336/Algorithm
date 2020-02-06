"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

"""
Time Complexity: O(n * 2^n)
Space Complexity: O(2^n)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []
        self.dfs(sorted(nums), 0, subset, results)
        return results

    # 递归的定义：
    # 找到所有以subset开头的所有子集
    # index 控制subset从第几个元素开始
    def dfs(self, nums, index, subset, results):
        # deep copy. subset之后会变，如果不用deep copy，results里的结果也会随着变化
        results.append(subset.copy())

        for i in range(index, len(nums)):
            # [] -> [1]
            subset.append(nums[i])

            # 把所有以[1]开头的子集放到results里
            self.dfs(nums, i + 1, subset, results)

            # [3] -> [], backtracking 回溯
            subset.pop()
