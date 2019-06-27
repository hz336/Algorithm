"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
"""


class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """

    def numDecodings(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return 0

        f = [0] * (len(s) + 1)
        f[0] = 1

        for i in range(1, len(s) + 1):
            if int(s[i - 1]) != 0:
                f[i] += f[i - 1]

            if i >= 2 and 10 <= int(s[i - 2: i]) <= 26:
                f[i] += f[i - 2]

        return f[-1]
