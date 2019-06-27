"""
Write a function, give a string A consisting of N characters and a string B consisting of M characters, returns the number of times A must be stated
such that B is a substring of the repeated string. If B can never be a substring of the repeated A, then your function should return -1.

Example
Given A = abcd, B = cdabcdab

your function should return 3, bcause after stating string A three times we obtain the string abcdabcdabcd. String B is a substring of this string.
"""


class Solution:
    """
    @param: : string A to be repeated
    @param: : string B
    @return: the minimum number of times A has to be repeated
    """

    def repeatedString(self, A, B):
        # write your code here
        if len(A) == 0:
            return -1

        if len(B) == 0:
            return 1

        s = ''
        q = 0
        while len(s) < len(B):
            s += A
            q += 1

        if s.find(B) >= 0:
            return q

        s += A
        if s.find(B) >= 0:
            return q + 1

        return -1

