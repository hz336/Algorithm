"""
Given a list of integers, which denote a permutation.

Find the previous permutation in ascending order.

Notice
The list may contains duplicate integers.

Example
For [1,3,2,3], the previous permutation is [1,2,3,3]
For [1,2,3,4], the previous permutation is [4,3,2,1]
"""


class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """

    def previousPermuation(self, nums):
        # write your code here
        if nums is None:
            return []

        if len(nums) <= 1:
            return nums

        i = len(nums) - 1
        while i:
            if i > 0 and nums[i - 1] > nums[i]:
                break
            i -= 1

        if i != 0:
            j = len(nums) - 1
            while j:
                if nums[i - 1] > nums[j]:
                    break
                j -= 1

            self.swap_item(nums, i - 1, j)

        self.swap_list(nums, i, len(nums) - 1)

        return nums

    def swap_item(self, nums, i, j):
        if 0 <= i < len(nums) and 0 <= j < len(nums):
            nums[i], nums[j] = nums[j], nums[i]

    def swap_list(self, nums, start, end):
        while start < end:
            self.swap_item(nums, start, end)
            start += 1
            end -= 1