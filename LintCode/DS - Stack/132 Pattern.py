"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm
that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Example
Given nums = [1, 2, 3, 4]
return False // There is no 132 pattern in the sequence.

Given nums = [3, 1, 4, 2]
return True // There is a 132 pattern in the sequence: [1, 4, 2].
"""

import math


class Solution:
    """
    @param: nums: a list of n integers
    @return: true if there is a 132 pattern or false
    """

    def find132pattern(self, nums):
        # write your code here
        stack = [-math.inf]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < stack[-1]:
                return True

            while stack and nums[i] > stack[-1]:
                v = stack.pop()

            stack.append(nums[i])
            stack.append(v)

        return False


