"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""


class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        if needle is None or len(needle) == 0:
            return 0

        if haystack is None or len(haystack) == 0 or len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            j = 0
            while haystack[i + j] == needle[j]:
                j += 1

                if j == len(needle):
                    return i

        return -1


