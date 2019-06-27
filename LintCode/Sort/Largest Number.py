"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example
Given [1, 20, 23, 4, 8], the largest formed number is 8423201.
"""


class LargerNumKey(str):
    def __lt__(x, y):       # x < y
        return x + y < y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey, reverse=True))
        return '0' if largest_num[0] == '0' else largest_num


sol = Solution()
ans = sol.largestNumber(nums=[1, 20, 23, 4, 8])
print(ans)
