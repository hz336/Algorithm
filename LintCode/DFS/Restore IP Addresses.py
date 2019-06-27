"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example
Given "25525511135", return

[
  "255.255.11.135",
  "255.255.111.35"
]
"""


class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """

    def restoreIpAddresses(self, s):
        # write your code here
        results = []
        self.dfs(s, 0, [], results)

        return results

    def dfs(self, s, index, subset, results):
        if len(subset) == 4:
            if index == len(s):
                results.append('.'.join(subset))
            return

        if index == len(s):
            return

        for i in range(index, len(s)):
            if i - index <= 3 and self.is_valid(s[index: i + 1]):
                subset.append(s[index: i + 1])
                self.dfs(s, i + 1, subset, results)
                subset.pop()

    def is_valid(self, s):
        if s == '0':
            return True
        elif s[0] != '0' and 0 <= int(s) < 256:
            return True
        else:
            return False