"""
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary

Notice
All words have the same length.
All words contain only lowercase alphabetic characters.

Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
"""

from collections import deque, defaultdict


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    """
    start -> end: bfs
    end -> start: dfs
    """

    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)

        mapping = defaultdict(list)
        distance = defaultdict(int)
        self.bfs(mapping, distance, start, end, dict)

        results = []
        path = []
        self.dfs(results, path, end, start, distance, mapping)

        return results

    def bfs(self, mapping, distance, start, end, dict):
        queue = deque([start])
        distance[start] = 0

        while queue:
            word = queue.popleft()
            next_words = self.expand(word, dict)
            for next_word in next_words:
                mapping[next_word].append(word)
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def dfs(self, results, path, curr, start, distance, mapping):
        path.append(curr)
        if curr == start:
            results.append(list(reversed(path)))
        else:
            for prev_word in mapping[curr]:
                if prev_word in distance and distance[curr] == distance[prev_word] + 1:
                    self.dfs(results, path, prev_word, start, distance, mapping)

        path.pop()

    def expand(self, word, dict):
        expansion = []
        for i in range(len(word)):
            part1, part2 = word[: i], word[i + 1:]
            for c in range(ord('a'), ord('z') + 1):
                if chr(c) != word[i]:
                    new_word = part1 + chr(c) + part2
                    if new_word in dict:
                        expansion.append(new_word)

        return expansion


