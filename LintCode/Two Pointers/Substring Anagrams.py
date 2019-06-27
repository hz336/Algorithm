"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 40,000.

The order of output does not matter.

Example
Given s = "cbaebabacd" p = "abc"

return [0, 6]

The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""


class Solution:
    """
    @param: s: a string
    @param: p: a string
    @return: a list of index
    """

    def findAnagrams(self, s, p):
        # write your code here
        results = []

        sums = [0] * 26
        for i in range(len(p)):
            sums[ord(p[i]) - ord('a')] += 1

        left = right = 0
        matched = 0
        while right < len(s):
            if sums[ord(s[right]) - ord('a')] >= 1:
                matched += 1
            sums[ord(s[right]) - ord('a')] -= 1
            right += 1

            if matched == len(p):
                results.append(left)

            if right - left == len(p):
                if sums[ord(s[left]) - ord('a')] >= 0:
                    matched -= 1
                sums[ord(s[left]) - ord('a')] += 1
                left += 1

        return results

