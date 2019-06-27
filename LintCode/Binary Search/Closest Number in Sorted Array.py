"""
Given a target number and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to the given target.
Return -1 if there is no element in the array.

Notice: There can be duplicate elements in the array, and we can return any of the indices with same value.
"""


class Solution:
    """
    @param: A: an integer array sorted in ascending order
    @param: target: An integer
    @return: an integer
    """

    def closestNumber(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if target - A[start] <= A[end] - target:
            return start
        else:
            return end







