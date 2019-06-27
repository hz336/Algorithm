"""
Given an array of integers, remove the duplicate numbers in it.

You should:
1. Do it in place in the array.
2. Move the unique numbers to the front of the array.
3. Return the total number of the unique numbers.

Example
Given nums = [1,3,1,4,4,2], you should:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

"""


class Solution:
    """
    @param: nums: an array of integers
    @return: the number of unique integers
    """

    # version 1. two pointers - O(1) memory
    def deduplication1(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        nums.sort()

        i = j = 0
        while i < len(nums) and j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1

            j += 1

        return i + 1

    # version 2. set - O(n) memory
    def deduplication2(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        uq_nums = set(nums)
        return len(uq_nums)

