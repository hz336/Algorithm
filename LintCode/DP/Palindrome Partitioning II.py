"""
Given a string s, cut s into some substrings such that every substring is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example
Given s = "aab",

Return 1 since the palindrome partitioning ["aa", "b"] could be produced using 1 cut.
"""

import math


class Solution:
    """
    @param s: A string
    @return: An integer
    """

    def minCut(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return 0

        palin = self.cal_palin(s)

        n = len(s)
        f = [math.inf] * (n + 1)
        f[0] = 0
        for curr in range(1, n + 1):
            for prev in range(curr):
                if palin[prev][curr - 1]:
                    f[curr] = min(f[curr], f[prev] + 1)

        return f[n] - 1

    def cal_palin(self, s):
        n = len(s)
        palin = [[False for _ in range(n)] for _ in range(n)]

        for mid in range(n):
            # old length
            start = end = mid
            while start >= 0 and end < n and s[start] == s[end]:
                palin[start][end] = True
                start -= 1
                end += 1

            # even length
            start = mid
            end = mid + 1
            while start >= 0 and end < n and s[start] == s[end]:
                palin[start][end] = True
                start -= 1
                end += 1

        return palin

