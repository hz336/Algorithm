"""
Given a decimal number n and an integer k, Convert decimal number n to base-k.

Notice
1.0<=n<=2^31-1, 2<=k<=16
2.Each letter over 9 is indicated in uppercase

Example
Example 1:
Given n = 5, k = 2
return "101"

Example 2:
Given n = 30, k = 16
return "1E"
"""


class Solution:
    """
    @param n: a decimal number
    @param k: a Integer represent base-k
    @return: a base-k number
    """

    def hexConversion(self, n, k):
        # write your code here
        if n == 0:
            return "0"

        result = ""
        while n > 0:
            t = n % k
            if t <= 9:
                c = chr(ord('0') + t)
            else:
                c = chr(ord('A') + t - 10)

            result = c + result
            n = n // k

        return result