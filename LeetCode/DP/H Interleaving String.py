"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""


"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        f = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    f[i][j] = True
                    continue

                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    f[i][j] = f[i][j] or f[i - 1][j]

                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    f[i][j] = f[i][j] or f[i][j - 1]

        return f[m][n]

