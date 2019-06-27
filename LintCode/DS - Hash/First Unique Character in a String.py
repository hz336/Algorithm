"""
Find the first unique character in a given string. You can assume that there is at least one unique character in the string.

Example
For "abaccdeff", return 'b'.
"""


class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        # Write your code here
        mapping = {}
        for index, value in enumerate(str):
            if value not in mapping:
                mapping[value] = index
            else:
                mapping[value] = -1

        min_index = len(str)
        for key, value in mapping.items():
            if value != -1 and value < min_index:
                min_index = value

        return str[min_index]




