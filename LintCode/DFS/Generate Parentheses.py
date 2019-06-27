"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example
Given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""


class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """

    def generateParenthesis(self, n):
        # write your code here
        results = []
        self.dfs(results, "", n, n)

        return results

    def dfs(self, results, paren, left, right):
        if left == 0 and right == 0:
            results.append(paren)
            return

        if left > 0:
            self.dfs(results, paren + "(", left - 1, right)

        if right > 0 and left < right:
            self.dfs(results, paren + ")", left, right - 1)


