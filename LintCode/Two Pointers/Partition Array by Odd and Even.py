"""
Partition an integers array into odd number first and even number second.
"""


class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """

    def partitionArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return

        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] % 2 == 1:
                left += 1

            while left <= right and nums[right] % 2 == 0:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
