"""
Given a string, find all permutations of it without duplicates.

Example
Given "abb", return ["abb", "bab", "bba"].

Given "aabb", return ["aabb", "abab", "baba", "bbaa", "abba", "baab"].
"""


class Solution:
    """
    @param str: A string
    @return: all permutations
    """

    def stringPermutation2(self, str):
        # write your code here
        if str is None:
            return []

        string = list(str)
        string.sort()
        visited = [False] * len(string)
        results = []
        self.dfs(string, [], visited, results)

        return results

    def dfs(self, string, subset, visited, results):
        if len(subset) == len(string):
            results.append(''.join(subset))

        for i in range(len(string)):
            if visited[i]:
                continue

            if i != 0 and string[i] == string[i - 1] and not visited[i - 1]:
                continue

            subset.append(string[i])
            visited[i] = True

            self.dfs(string, subset, visited, results)

            subset.pop()
            visited[i] = False