"""
Giving a string with number from 1-n in random order, but miss 1 number. Find that number.

Example
Given n = 20, str = 19201234567891011121314151618

return 17
"""


class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """

    def findMissing(self, nums):
        # write your code here
        N = len(nums)
        total = (0 + N) * (N + 1) // 2
        cur_sum = sum(nums)

        return total - cur_sum