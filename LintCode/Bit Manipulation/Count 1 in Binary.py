"""
Count how many 1 in binary representation of a 32-bit integer.

Example
Given 32, return 1
Given 5, return 2
Given 1023, return 9
"""


class Solution:
    """
    @param: num: An integer
    @return: An integer
    """

    def countOnes(self, num):
        # write your code here
        count = 0
        for i in range(32):
            if num & (1 << i) != 0:
                count += 1

        return count