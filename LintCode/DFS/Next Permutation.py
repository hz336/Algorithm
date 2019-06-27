"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

Example
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Challenge
The replacement must be in-place, do not allocate extra memory.
"""


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """

    def nextPermutation(self, nums):
        # write your code here
        if nums is None:
            return []

        if len(nums) <= 1:
            return nums

        i = len(nums) - 1
        while i:
            if i > 0 and nums[i] > nums[i - 1]:
                break
            i -= 1

        if i != 0:
            j = len(nums) - 1
            while j:
                if nums[i - 1] < nums[j]:
                    self.swap_items(nums, i - 1, j)
                    break
                j -= 1

        self.swap_list(nums, i, len(nums) - 1)

        return nums

    def swap_items(self, nums, i, j):
        if 0 <= i < len(nums) and 0 <= j < len(nums):
            nums[i], nums[j] = nums[j], nums[i]

    def swap_list(self, nums, start, end):
        if 0 <= start < len(nums) and 0 <= end < len(nums):
            while start < end:
                self.swap_items(nums, start, end)
                start += 1
                end -= 1

