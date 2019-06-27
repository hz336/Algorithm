"""
Determine the number of bits required to flip if you want to convert integer n to integer m.

Notice
Both n and m are 32-bit integers.

Example
Given n = 31 (11111), m = 14 (01110), return 2.
"""


class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """

    def bitSwapRequired(self, a, b):
        # write your code here
        c = a ^ b
        count = 0
        for i in range(32):
            if c & (1 << i) != 0:
                count += 1

        return count
