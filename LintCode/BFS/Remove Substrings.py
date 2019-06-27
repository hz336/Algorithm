"""
Given a string s and a set of n substrings. You are supposed to remove every instance of those n substrings from s so that s is of the minimum length
and output this minimum length.

Example
Given s = ccdaabcdbb, substrs = ["ab", "cd"]
Return 2

Explanation:
ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)
"""

from collections import deque


class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """

    def minLength(self, s, dict):
        # write your code here
        min_len = len(s)
        queue = deque([s])
        visited = {s, }
        while queue:
            string = queue.popleft()
            for seq in dict:
                found = string.find(seq)
                while found != -1:
                    new_string = string[: found] + string[found + len(seq):]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append(new_string)
                        min_len = min(min_len, len(new_string))

                    found = string.find(seq, found + 1)

        return min_len






