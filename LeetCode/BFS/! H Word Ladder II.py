"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such
that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

"""
There’s a good theoretical paper on how to mix short and long term signals in your alpha model (Prop 4 is relevant):
http://faculty.haas.berkeley.edu/garleanu/DynTrad.pdf

At a very intuitive level, we annualize our alphas by multiplying by 12. 
This makes sense if the autocorr of alpha is 100%, but the autocorr will be much lower if alpha is driven by short term factors.

Therefore, eventually we will have to introduce a new penalty parameter (k), where final coef = coef * (1 + k*(signal autocorr-1))
I think adding this parameter to  ‘sbs_floor’ would be relatively easy. But let’s hold off until we finish prelim backtests using seasonality.

"""

from collections import deque, defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or endWord not in wordList:
            return []

        wordDict = {word for word in wordList}
        distance = defaultdict(list)
        mapping = defaultdict(list)
        self.bfs(beginWord, wordDict, distance, mapping)

        results = []
        path = []
        self.dfs(results, path, endWord, beginWord, distance, mapping)

        return results

    def bfs(self, beginWord, wordDict, distance, mapping):
        queue = deque([beginWord])
        distance[beginWord] = 0
        while queue:
            curr_word = queue.popleft()
            next_words = self.expand(curr_word, wordDict)
            for next_word in next_words:
                mapping[next_word].append(curr_word)
                if next_word not in distance:
                    distance[next_word] = distance[curr_word] + 1
                    queue.append(next_word)

    def expand(self, word, wordDict):
        next_words = []
        for i in range(len(word)):
            part1, part2 = word[:i], word[i + 1:]
            for c in range(ord('a'), ord('z') + 1):
                if chr(c) != word[i]:
                    new_word = part1 + chr(c) + part2
                    if new_word in wordDict:
                        next_words.append(new_word)

        return next_words

    def dfs(self, results, path, curr, start, distance, mapping):
        if curr == start:
            results.append([start] + path[::-1])

        for prev_word in mapping[curr]:
            if distance[curr] == distance[prev_word] + 1:
                path.append(curr)
                self.dfs(results, path, prev_word, start, distance, mapping)
                path.pop()




