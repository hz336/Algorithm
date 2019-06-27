"""
Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one
character or two characters. Output all possible results.

Example
Given the string "123"
return [["1","2","3"],["12","3"],["1","23"]]
"""


class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if s is None:
            return []

        if len(s) == 0:
            return [[]]

        results = []
        self.dfs(s, 0, [], results)

        return results

    def dfs(self, s, index, subset, results):
        if index == len(s):
            results.append(subset.copy())

        for step in range(1, 3):
            if index + step <= len(s):
                substr = s[index: index + step]
                subset.append(substr)
                self.dfs(s, index + step, subset, results)
                subset.pop()

