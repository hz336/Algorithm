"""
Given a permutation which may contain repeated numbers, find its index in all the permutations of these numbers, which are ordered in lexicographical
order. The index begins at 1.
"""

from collections import defaultdict


class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    def permutationIndexII(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        index, factor, multi_fact = 1, 1, 1
        counter = defaultdict(int)

        for i in range(len(nums) - 1, -1, -1):
            # count numbers that are smaller than nums[i]
            count = 0
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    count += 1

            counter[nums[i]] += 1
            multi_fact *= counter[nums[i]]
            index += count * factor // multi_fact
            factor *= (len(nums) - i)

        return index

