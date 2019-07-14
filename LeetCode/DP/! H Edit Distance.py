"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)

        m, n = len(word1), len(word2)
        f = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    f[i][j] = j
                    continue

                if j == 0:
                    f[i][j] = i
                    continue

                f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])

        return f[m][n]


"""
Time Complexity: O(mn)
Space Complexity: O(n)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)

        m, n = len(word1), len(word2)
        f = [[float('inf') for _ in range(n + 1)] for _ in range(2)]
        old, now = 0, 1

        for i in range(m + 1):
            old, now = now, old
            for j in range(n + 1):
                if i == 0:
                    f[now][j] = j
                    continue

                if j == 0:
                    f[now][j] = i
                    continue

                f[now][j] = min(f[old][j], f[now][j - 1], f[old][j - 1]) + 1
                if word1[i - 1] == word2[j - 1]:
                    f[now][j] = min(f[now][j], f[old][j - 1])

        return f[now][n]

