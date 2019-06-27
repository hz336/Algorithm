"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""


class Solution:
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


"""
Time Complexity: O(mn)
Space Complexity: O(mn)
    Optimal space complexity can be O(2m), but O(m) is not possible. 
"""
class Solution_v2:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    def isMatch(self, s, p):
        # write your code here
        if s is None or p is None:
            return False

        m = len(s)
        n = len(p)
        f = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    f[i][j] = True
                    continue

                if i > 0 and j == 0:
                    f[i][j] = False
                    continue

                if i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '?'):
                    f[i][j] = f[i - 1][j - 1]

                if p[j - 1] == '*':
                    f[i][j] = f[i][j] or f[i][j - 1]
                    if i > 0:
                        f[i][j] = f[i][j] or f[i - 1][j]

        return f[m][n]
