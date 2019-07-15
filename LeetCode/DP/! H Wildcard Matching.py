"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""


"""
最值型DP
Time Complexity: O(mn)
Space Complexity: O(mn), 滚动数组可以做到O(2n)，但是做到不O(n)
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
                    if i > 0 and (p[j - 1] == '?' or s[i - 1] == p[j - 1]):
                        f[i][j] = f[i][j] or f[i - 1][j - 1]
                else:
                    # * means zero
                    f[i][j] = f[i][j] or f[i][j - 1]

                    # * means at least one character
                    if i >= 1:
                        f[i][j] = f[i][j] or f[i - 1][j]

        return f[m][n]



"""
DFS with memorization (Maybe can be ignored)
"""
class Solution:
    def isMatch(self, s, p):
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






