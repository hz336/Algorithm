"""
Given a string s and a dictionary of words dict, determine if s can be break into a space-separated sequence of one or more dictionary words.

Example
Given s = "lintcode", dict = ["lint", "code"].

Return true because "lintcode" can be break as "lint code".
"""


class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """

    def wordBreak(self, s, dict):
        # write your code here
        if len(dict) == 0:
            return len(s) == 0

        n = len(s)
        breakable = [False] * (n + 1)
        breakable[0] = True

        max_len = max([len(word) for word in dict])
        for i in range(1, len(s) + 1):
            for j in range(1, min(i, max_len) + 1):
                if not breakable[i - j]:
                    continue

                if s[i - j: i] in dict:
                    breakable[i] = True
                    break

        return breakable[n]