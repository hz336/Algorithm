"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""


class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        left = 0
        count = 1

        for right in range(1, len(nums)):
            if count == 1:
                left += 1
                nums[left] = nums[right]
                if nums[left] == nums[left - 1]:
                    count += 1
            else:
                if nums[left] != nums[right]:
                    left += 1
                    nums[left] = nums[right]
                    count = 1
                else:
                    continue

        return left + 1
