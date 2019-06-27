"""
Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

Notice
You are not necessary to keep the original order of positive integers or negative integers.

Example
Given [-1, -2, -3, 4, 5, 6], after re-range, it will be [-1, 5, -2, 4, -3, 6] or any other reasonable answer.
"""


class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """

    def rerange(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return None

        left, right = 0, len(A) - 1
        while left <= right:
            while left <= right and A[left] < 0:
                left += 1

            while left <= right and A[right] > 0:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        num_neg = left
        num_pos = len(A) - right - 1

        if abs(num_neg - num_pos) > 1:
            return

        if num_neg > num_pos:
            left = 1
            right = len(A) - 1
        elif num_neg < num_pos:
            left = 0
            right = len(A) - 2
        else:
            left = 1
            right = len(A) - 2

        while left <= right:
            A[left], A[right] = A[right], A[left]
            left += 2
            right -= 2
