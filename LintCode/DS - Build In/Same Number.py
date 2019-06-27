"""
Given an array, If the same number exists in the array, and the distance of the same number is less than the given value k, output YES, otherwise
output NO.

Example
Given array = [1,2,3,1,5,9,3], k = 4, return "YES".

Explanation:
The distance of 1 whose indexes are  3 and 0 is 3, which meets the requirement and output YES.
Given array =[1,2,3,5,7,1,5,1,3], k = 4, return "YES".

Explanation:
The distance of 1 whose indexes are  7 and 5 is 2, which meets the requirement and output YES.
"""

import math


class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """

    def sameNumber(self, nums, k):
        # Write your code here

        min_diff = math.inf
        mapping = {}
        for index, value in enumerate(nums):
            if value not in mapping:
                mapping[value] = index
            else:
                diff = index - mapping[value]
                if diff < min_diff:
                    min_diff = diff
                mapping[value] = index

        if min_diff < k:
            return "YES"

        return "NO"
