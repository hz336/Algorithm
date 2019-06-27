"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example
Given s = "bbbab" return 4
One possible longest palindromic subsequence is "bbbb".
"""


class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    def longestPalindromeSubseq(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return 0

        n = len(s)
        f = [[0 for _ in range(n)] for _ in range(n)]

        # length == 1
        for i in range(n):
            f[i][i] = 1

        # length == 2
        for i in range(n - 1):
            f[i][i + 1] = f[i][i]
            if s[i] == s[i + 1]:
                f[i][i + 1] = 2

        # length >= 3
        for l in range(3, n + 1):
            # start position
            for start in range(n - l + 1):
                # end position
                end = start + l - 1
                f[start][end] = max(f[start][end - 1], f[start + 1][end])
                if s[start] == s[end]:
                    f[start][end] = max(f[start][end], f[start + 1][end - 1] + 2)

        return f[0][n - 1]

