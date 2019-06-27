"""
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.
"""


class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1

        if len(target) == 0:
            return 0

        if len(target) > len(source):
            return -1

        for i in range(len(source) - len(target) + 1):
            j = 0
            while source[i + j] == target[j]:
                j += 1

                if j == len(target):
                    return i

        return -1


