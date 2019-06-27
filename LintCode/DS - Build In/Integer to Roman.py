"""
Given an integer, convert it to a roman numeral.

The number is guaranteed to be within the range from 1 to 3999.

https://en.wikipedia.org/wiki/Roman_numerals
"""


class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """

    def intToRoman(self, n):
        # write your code here
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        s = ''
        digit = 0
        while n:
            times = n // nums[digit]
            n -= nums[digit] * times
            s += roman[digit] * times
            digit += 1

        return s
