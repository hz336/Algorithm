"""
Implement function atoi to convert a string to an integer.

If no valid conversion could be performed, a zero value is returned.

If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Example
    "10" => 10
    "-1" => -1
    "123123123123123" => 2147483647
    "1.0" => 1
"""


class Solution:
    """
    @param: str: A string
    @return: An integer
    """

    def atoi(self, str):
        # write your code here
        if str is None or len(str) == 0:
            return 0

        sign, p, nums = 1, 0, 0
        imin, imax = -2 ** 31, 2 ** 31 - 1

        while str[p] == ' ':
            p += 1

        if str[p] == '+' or str[p] == '-':
            sign = 1 if str[p] == '+' else 0
            p += 1

        while p < len(str) and '0' <= str[p] <= '9':
            nums = nums * 10 + ord(str[p]) - ord('0')

            x = nums if sign else -nums
            if x < imin: return imin
            if x > imax: return imax

            p += 1

        return nums if sign else -nums

