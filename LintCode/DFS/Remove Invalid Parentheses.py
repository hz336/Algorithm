"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

 Notice
The input string may contain letters other than the parentheses ( and ).

Example
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""


class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        self.dfs(s, results, 0, 0, ('(', ')'))
        return results

    def dfs(self, s, results, last_i, last_j, par):
        count = 0
        for i in range(last_i, len(s)):
            count += (s[i] == par[0]) - (s[i] == par[1])
            if count >= 0:
                continue
            for j in range(last_j, i + 1):
                if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                    self.dfs(s[:j] + s[j + 1:], results, i, j, par)
            return

        reversed_s = s[::-1]

        if par[0] == '(':
            self.dfs(reversed_s, results, 0, 0, (')', '('))
        else:
            results.append(reversed_s)