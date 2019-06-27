"""
Validate if a given string is numeric.
"""


class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """

    def isNumber(self, s):
        # write your code here
        if s is None:
            return False

        s = s.strip()
        if len(s) == 0:
            return False

        start, end = 0, len(s) - 1
        if s[start] == '+' or s[start] == '-':
            start += 1

        n_digit = n_dot = 0
        while start <= end and (s[start].isdigit() or s[start] == '.'):
            if s[start].isdigit():
                n_digit += 1
            if s[start] == '.':
                n_dot += 1

            start += 1

        if n_digit <= 0 or n_dot > 1:
            return False

        if start <= end and s[start] == 'e':
            start += 1
            if start <= end and (s[start] == '+' or s[start] == '-'):
                start += 1

            if start <= end:
                for i in range(start, end + 1):
                    if not s[start].isdigit():
                        return False

        return True

