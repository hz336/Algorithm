"""
Description
Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order,
lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

https://en.wikipedia.org/wiki/Longest_increasing_subsequence

Example
For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4

Challenge
Time complexity O(n^2) or O(nlogn)
"""

import math

"""
Dynamic Programming + Binary Search 
Just remember the algorithm 
Time Complexity: O(nlogn)
"""
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    """
    For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

    len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
    len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
    len = 3   :      [4, 5, 6]            => tails[2] = 6
    We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.

    Each time we only do one of the two:

    (1) if x is larger than all tails, append it, increase the size by 1
    (2) if tails[i-1] < x <= tails[i], update tails[i]
    """

    def longestIncreasingSubsequence(self, A):
        if A is None or len(A) == 0:
            return 0

        len_A = len(A)
        min_last = [math.inf] * (len_A + 1)
        min_last[0] = -math.inf

        for i in range(len_A):
            # find the first number in minLast >= nums[i]
            index = self.binary_search(min_last, A[i])
            min_last[index] = A[i]

        for i in range(len_A, 0, -1):
            if min_last[i] != math.inf:
                return i

        return 0

    def binary_search(self, min_last, target):
        start, end = 0, len(min_last) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if min_last[mid] < target:
                start = mid
            else:
                end = mid

        if min_last[start] >= target:
            return start
        else:
            return end

