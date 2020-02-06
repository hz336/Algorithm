"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        subset = []
        results = []
        self.dfs(s, 0, subset, results)
        return results

    def dfs(self, s, index, subset, results):
        if index == len(s):
            results.append(subset)
            return

        for i in range(index, len(s)):
            if self.is_valid(s[index: i + 1]):
                self.dfs(s, i + 1, subset + [s[index: i + 1]], results)

    def is_valid(self, s):
        start, end = 0, len(s) - 1
        while start <= end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1

        return True
