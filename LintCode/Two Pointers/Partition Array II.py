"""
Partition an unsorted integer array into three parts:

The front part < low
The middle part >= low & <= high
The tail part > high
Return any of the possible solutions.
"""


class Solution:
    """
    @param: nums: an integer array
    @param: low: An integer
    @param: high: An integer
    @return:
    """

    def partition2(self, nums, low, high):
        # write your code here
        if nums is None or len(nums) == 0:
            return

        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < low:
                left += 1

            while left <= right and nums[right] > high:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

