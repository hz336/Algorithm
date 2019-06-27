"""
Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical
order. The index begins at 1.

Example
Given [1,2,4], return 1.
"""


class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    # http://www.cnblogs.com/theskulls/p/4881142.html
    def permutationIndex(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        index, factor = 1, 1
        for i in range(len(nums) - 1, -1, -1):
            # count numbers that are smaller than nums[i]
            count = 0
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    count += 1

            index += count * factor
            factor *= (len(nums) - i)

        return index