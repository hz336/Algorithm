"""
Given a string, find the length of the longest substring without repeating characters.
"""


class Solution:
    """
    @param s: a string
    @return: an integer
    """

    def lengthOfLongestSubstring(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return 0

        last = {}
        left = ans = 0
        for i in range(len(s)):
            if s[i] in last and last[s[i]] >= left:
                left = last[s[i]] + 1

            last[s[i]] = i

            ans = max(ans, i - left + 1)

        return ans

