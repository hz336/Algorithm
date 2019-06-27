"""
Given an integer array nums with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer
target.

Example
Given nums = [1, 2, 4], target = 4

The possible combination ways are:
[1, 1, 1, 1]
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
[2, 2]
[4]
return 6
"""

"""
Time Complexity: O(mn)
Space complexity: O(m)
"""
class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    def backPackVI(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        n = len(nums)
        f = [0] * (target + 1)
        f[0] = 1

        # 先看所有的重量，再去枚举最后一个物品是谁
        for weight in range(1, target + 1):
            for item in range(1, n + 1):
                if weight >= nums[item - 1]:
                    f[weight] += f[weight - nums[item - 1]]

            print(f)

        return f[target]


target = 7
nums = [2,3,6,7]
sol = Solution()
ans = sol.backPackVI(nums, target)
