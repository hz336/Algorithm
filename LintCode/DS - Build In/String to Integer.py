"""
Given a string, convert it to an integer. You may assume the string is a valid integer number that can be presented by a signed 32bit integer
(-231 ~ 231-1).
"""


class Solution:
    """
    @param: str: A string
    @return: An integer
    """

    def stringToInteger(self, str):
        # write your code here

        num, sig = 0, 1

        if str[0] == '-':
            sig = -1
            str = str[1:]

        for c in str:
            num = num * 10 + ord(c) - ord('0')

        return sig * num

