"""
Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.

Example
For "ABCD" and "EDCA", the LCS is "A" (or "D", "C"), return 1.

For "ABCD" and "EACB", the LCS is "AC", return 2.
"""

"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""
class Solution:
    def longestCommonSubsequence(self, A, B):
        if A is None or B is None or len(A) == 0 or len(B) == 0:
            return 0

        m, n = len(A), len(B)
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    continue

                f[i][j] = max(f[i - 1][j], f[i][j - 1])
                if A[i - 1] == B[j - 1]:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)

        return f[m][n]
