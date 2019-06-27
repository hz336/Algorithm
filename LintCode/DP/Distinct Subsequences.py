"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without
disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example
Given S = "rabbbit", T = "rabbit", return 3.

Challenge
Do it in O(n2) time and O(n) memory.

O(n2) memory is also acceptable if you do not know how to optimize memory.
"""


class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        # write your code here
        if S is None or T is None:
            return 0

        m = len(S)
        n = len(T)
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                # if T is empty
                if j == 0:
                    f[i][j] = 1
                    continue

                if i == 0 and j > 0:
                    f[i][j] = 0
                    continue

                f[i][j] = f[i - 1][j]
                if S[i - 1] == T[j - 1]:
                    f[i][j] += f[i - 1][j - 1]

        return f[m][n]



