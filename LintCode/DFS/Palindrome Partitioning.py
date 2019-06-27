"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example
Given s = "aab", return:

[
  ["aa","b"],
  ["a","a","b"]
]
"""

""" TODO: DP version """
class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def partition(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return []

        results = []
        self.dfs(s, 0, [], results)

        return results

    def dfs(self, s, index, partition, results):
        if index == len(s):
            results.append(partition.copy())
            return

        for i in range(index, len(s)):
            substr = s[index: i + 1]
            if not self.is_palindrome(substr):
                continue

            partition.append(substr)
            self.dfs(s, i + 1, partition, results)
            partition.pop()

    def is_palindrome(self, string):
        start, end = 0, len(string) - 1
        while start < end:
            if string[start] != string[end]:
                return False

            start += 1
            end -= 1

        return True
