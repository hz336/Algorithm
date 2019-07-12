"""
Given n items with size nums[i] which an integer array and all positive numbers. An integer target denotes the size of a backpack. Find the number of
possible fill the backpack.

Each item may only be used once

Example
Given candidate items [1,2,3,3,7] and target 7,

A solution set is:
[7]
[1, 3, 3]
return 2
"""

"""
Time Complexity: O(mn)
Space complexity: O(m)
"""
class Solution:
    def backPackV(self, nums, target):
        if nums is None or len(nums) == 0:
            return 0

        n = len(nums)
        f = [0] * (target + 1)
        f[0] = 1

        for item in range(1, n + 1):
            for weight in range(target, -1, -1):
                if weight >= nums[item - 1]:
                    f[weight] += f[weight - nums[item - 1]]

            print(f)

        return f[target]


target = 7
nums = [2, 3, 6, 7]
sol = Solution()
ans = sol.backPackV(nums, target)
