"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Notice
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Example
Given pattern = "abba", str = "dog cat cat dog", return true.
Given pattern = "abba", str = "dog cat cat fish", return false.
Given pattern = "aaaa", str = "dog cat cat dog", return false.
Given pattern = "abba", str = "dog dog dog dog", return false.
"""


class Solution:
    """
    @param pattern: a string, denote pattern string
    @param str: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """

    def wordPattern(self, pattern, string):
        # write your code here
        pattern_list = list(pattern)
        string_list = string.split()

        if len(pattern_list) != len(string_list):
            return False

        mapping = {}
        for i in range(len(pattern_list)):
            if pattern_list[i] not in mapping:
                mapping[pattern_list[i]] = string_list[i]
            else:
                if mapping[pattern_list[i]] != string_list[i]:
                    return False

        mapping = {}
        for i in range(len(pattern_list)):
            if string_list[i] not in mapping:
                mapping[string_list[i]] = pattern_list[i]
            else:
                if mapping[string_list[i]] != pattern_list[i]:
                    return False

        return True