"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []

        results = []
        subset = []
        self.dfs(n, 0, 0, subset, results)
        return results

    def dfs(self, n, left, right, subset, results):
        if len(subset) == n * 2:
            results.append(''.join(subset))

        if left < n:
            self.dfs(n, left + 1, right, subset + ['('], results)

        if right < left:
            self.dfs(n, left, right + 1, subset + [')'], results)

