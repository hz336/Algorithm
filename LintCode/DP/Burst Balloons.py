"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the
balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the
burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example
Given [4, 1, 5, 10]
Return 270

nums = [4, 1, 5, 10] burst 1, get coins 4 * 1 * 5 = 20
nums = [4, 5, 10]    burst 5, get coins 4 * 5 * 10 = 200
nums = [4, 10]       burst 4, get coins 1 * 4 * 10 = 40
nums = [10]          burst 10, get coins 1 * 10 * 1 = 10

Total coins 20 + 200 + 40 + 10 = 270
"""

"""
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""
class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """

    def maxCoins(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        nums = [1] + nums + [1]
        n = len(nums)
        f = [[0 for _ in range(n)] for _ in range(n)]

        for length in range(2, n):
            for start in range(n - length):
                end = start + length
                for k in range(start + 1, end):
                    f[start][end] = max(f[start][end], f[start][k] + f[k][end] + nums[start] * nums[k] * nums[end])

        return f[0][n - 1]
