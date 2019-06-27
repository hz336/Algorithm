"""
Given two strings, write a method to decide if one is a permutation of the other.

Example
abcd is a permutation of bcad, but abbe is not a permutation of abe
"""

from collections import defaultdict


class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """

    def Permutation(self, A, B):
        # write your code here
        if A is None or B is None:
            return False

        if len(A) != len(B):
            return False

        mapping = defaultdict(int)
        for index, key in enumerate(A):
            mapping[key] += 1

        for index, key in enumerate(B):
            mapping[key] -= 1

        for key, value in mapping.items():
            if value != 0:
                return False

        return True
