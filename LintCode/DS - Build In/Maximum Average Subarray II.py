"""
Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.

Notice
It's guaranteed that the size of the array is greater or equal to k.

Example
Given nums = [1, 12, -5, -6, 50, 3], k = 3
Return 15.667 // (-6 + 50 + 3) / 3 = 15.667
"""


class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """

    def maxAverage(self, nums, k):
        # write your code here
        start = -1e10
        end = 1e10
        eps = 1e-3

        while end - start > eps:
            mid = start + (end - start) / 2
            if self.check(nums, mid, k):
                start = mid
            else:
                end = mid
            print(mid)

        return start

    def check(self, nums, avg, k):
        total = [0]
        num_min = [0]
        for i in range(1, len(nums) + 1):
            total.append(total[i - 1] + (nums[i - 1] - avg))
            num_min.append(min(num_min[i - 1], total[i]))

            if i >= k and total[i] - num_min[i - k] >= 0:
                return True

        return False


sol = Solution()
ans = sol.maxAverage(nums=[1, 12, -5, -6, 50, 3], k = 3)
print(ans)
