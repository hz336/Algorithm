"""
Given an array of strings, return all groups of strings that are anagrams.

Notice
All inputs will be in lower-case

Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Challenge
What is Anagram?
- Two strings are anagram if they can be the same after change the order of characters.
"""

from collections import defaultdict


class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        # write your code here
        mapping = defaultdict(list)
        for word in strs:
            new_word = ''.join(sorted(word))
            mapping[new_word].append(word)

        results = []
        for key, value in mapping.items():
            if len(value) >= 2:
                results += value

        return results
