"""
Given a string of numbers, write a function to find the maximum value from the string, you can add a + or * sign between any two numbers.

Example
Given str = 01231, return 10
((((0 + 1) + 2) * 3) + 1) = 10 we get the maximum value 10

Given str = 891, return 73
As 8 * 9 * 1 = 72 and 8 * 9 + 1 = 73 so 73 is maximum.
"""

class Solution:
    """
    @param: : the given string
    @return: the maximum value
    """

    def calcMaxValue(self, str):
        # write your code here
        if len(str) == 0:
            return 0

        result = int(str[0])
        for i in range(1, len(str)):
            if str[i] == '0' or str[i] == '1' or result <= 1:
                result += int(str[i])
            else:
                result *= int(str[i])

        return result


