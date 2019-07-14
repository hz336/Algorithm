"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

"""
DP
Time Complexity: O(mn)
Space Complexity: O(mn)

这道题里面 i vs 0, j vs 1 and j vs 2很容易出错
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s is None or p is None:
            return False

        m, n = len(s), len(p)
        f = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                # p is an empty regexp
                if j == 0:
                    f[i][j] = i == 0
                    continue

                if p[j - 1] != '*':
                    if i > 0 and (p[j - 1] == '.' or s[i - 1] == p[j - 1]):
                        f[i][j] = f[i][j] or f[i - 1][j - 1]
                else:
                    if j >= 2:
                        # c* means zero c
                        f[i][j] = f[i][j] or f[i][j - 2]

                        # c* means at least one c, and c matches s[i - 1]
                        if p[j - 2] == '.' or (i >= 1 and p[j - 2] == s[i - 1]):
                            f[i][j] = f[i][j] or f[i - 1][j]

        return f[m][n]



"""
Maybe can be ignored
DFS with memorization 
"""
class Solution_v1:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, s, p):
        # write your code here
        if s is None or p is None:
            return False

        memo = [[False for _ in range(len(p))] for _ in range(len(s))]
        visited = [[False for _ in range(len(p))] for _ in range(len(s))]
        match = self.dfs(s, 0, p, 0, memo, visited)

        return match

    def dfs(self, s, s_index, p, p_index, memo, visited):
        if s_index == len(s):
            return self.all_star(p, p_index)

        if p_index == len(p):
            return s_index == len(s)

        if visited[s_index][p_index]:
            return memo[s_index][p_index]

        if p[p_index] == '*':
            # '*' matches empty | one character
            match = self.dfs(s, s_index, p, p_index + 1, memo, visited) or self.dfs(s, s_index + 1, p, p_index, memo, visited)
        else:
            match = self.char_match(s[s_index], p[p_index]) and self.dfs(s, s_index + 1, p, p_index + 1, memo, visited)

        visited[s_index][p_index] = True
        memo[s_index][p_index] = match

        return match

    def all_star(self, p, p_index):
        for i in range(p_index, len(p)):
            if p[i] != '*':
                return False

        return True

    def char_match(self, s_char, p_char):
        return s_char == p_char or p_char == '?'
















