"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to
s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)

Notice
You may assume both pattern and str contains only lowercase letters.

Example
Given pattern = "abab", str = "redblueredblue", return true.
Given pattern = "aaaa", str = "asdasdasdasd", return true.
Given pattern = "aabb", str = "xyzabcxzyabc", return false.
"""


class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    def wordPatternMatch(self, pattern, string):
        # write your code here
        mapping = {}
        hashset = set()
        is_valid = self.dfs(pattern, 0, string, 0, mapping, hashset)

        return is_valid

    def dfs(self, pattern, pattern_idx, string, string_idx, mapping, hashset):
        if len(pattern) == pattern_idx and len(string) == string_idx:
            return True

        if len(pattern) == pattern_idx or len(string) == string_idx:
            return False

        key = pattern[pattern_idx]
        if key in mapping:
            value = mapping[key]
            if not string.startswith(value, string_idx):
                return False

            is_valid = self.dfs(pattern, pattern_idx + 1, string, string_idx + len(value), mapping, hashset)
            return is_valid

        for i in range(string_idx, len(string)):
            value = string[string_idx: i + 1]

            if value in hashset:
                continue

            mapping[key] = value
            hashset.add(value)

            # continue to match the rest
            is_valid = self.dfs(pattern, pattern_idx + 1, string, string_idx + len(value), mapping, hashset)
            if is_valid:
                return True

            mapping.pop(key)
            hashset.remove(value)

        return False



