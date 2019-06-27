"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible
strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
"""


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        results = []
        subset = []
        self.dfs(S, 0, subset, results)
        return results

    def dfs(self, S, index, subset, results):
        if len(subset) == len(S):
            results.append(''.join(subset))

        for i in range(index, len(S)):
            if not S[i].isalpha():
                self.dfs(S, i + 1, subset + [S[i]], results)
            else:
                self.dfs(S, i + 1, subset + [S[i].lower()], results)
                self.dfs(S, i + 1, subset + [S[i].upper()], results)

