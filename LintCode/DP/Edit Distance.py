"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example
Given word1 = "mart" and word2 = "karma", return 3.
"""

"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""
class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """

    def minDistance(self, word1, word2):
        # write your code here
        if word1 is None or word2 is None:
            return 0

        m = len(word1)
        n = len(word2)
        f = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    f[i][j] = 0
                    continue

                if i == 0 and j > 0:
                    f[i][j] = j
                    continue

                if i > 0 and j == 0:
                    f[i][j] = i
                    continue

                f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])

        return f[m][n]