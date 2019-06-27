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
        if s is None or len(s) == 0:
            return []

        subset = []
        results = []
        self.dfs(s, subset, 0, results)
        return results

    def dfs(self, s, subset, index, results):
        if index == len(s):
            results.append(subset.copy())

        for i in range(index, len(s)):
            sub_str = s[index: i + 1]
            if not self.is_palindrome(sub_str):
                continue

            subset.append(sub_str)
            self.dfs(s, subset, i + 1, results)
            subset.pop()

    def is_palindrome(self, string):
        start, end = 0, len(string) - 1
        while start < end:
            if string[start] != string[end]:
                return False

            start += 1
            end -= 1

        return True
