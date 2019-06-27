"""
Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.

Example
For s1 = "aabcc", s2 = "dbbca"

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Challenge
O(n2) time or better
"""

"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""
class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """

    def isInterleave(self, s1, s2, s3):
        # write your code here
        if s1 is None or s2 is None or s3 is None:
            return False

        m = len(s1)
        n = len(s2)
        if len(s3) != m + n:
            return False

        f = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    f[i][j] = True
                    continue

                if i > 0 and s3[i + j - 1] == s1[i - 1]:
                    f[i][j] = f[i][j] or f[i - 1][j]

                if j > 0 and s3[i + j - 1] == s2[j - 1]:
                    f[i][j] = f[i][j] or f[i][j - 1]

        return f[m][n]

