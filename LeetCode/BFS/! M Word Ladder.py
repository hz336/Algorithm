"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord,
such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from collections import deque

"""
Bidirectional BFS:
The idea behind bidirectional search is to run two simultaneous searches—one forward from
the initial state and the other backward from the goal—hoping that the two searches meet in
the middle. The motivation is that b^(d/2) + b^(d/2) is much less than b^d. b is branch factor, d is depth. 

Time Complexity: O(length of words * length of word list)
Space Complexity: O(length of words * length of word list)
"""

class Solution_v2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        wordDict = {item for item in wordList}
        len_word = len(beginWord)
        queue_begin, queue_end = deque([(beginWord, 1)]), deque([(endWord, 1)])
        visited_begin, visited_end = {beginWord: 1}, {endWord: 1}

        while queue_begin and queue_end:
            # Change begin word
            ans = self.bfs(len_word, wordDict, queue_begin, visited_begin, visited_end)
            if ans:
                return ans

            # Change end word
            ans = self.bfs(len_word, wordDict, queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0

    def bfs(self, len_word, wordDict, queue, visited, visited_other):
        word, steps = queue.popleft()
        for i in range(len_word):
            part1, part2 = word[:i], word[i + 1:]
            for c in range(ord('a'), ord('z') + 1):
                if chr(c) != word[i]:
                    new_word = part1 + chr(c) + part2
                    if new_word in visited_other:
                        return steps + visited_other[new_word]

                    if new_word in wordDict:
                        queue.append((new_word, steps + 1))
                        visited[new_word] = steps + 1
                        wordDict.remove(new_word)

        return 0


"""
BFS
Time Complexity: O(length of words * length of word list)
Space Complexity: O(length of words * length of word list)
"""
class Solution_v1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        wordDict = {item for item in wordList}
        len_word = len(beginWord)
        queue = deque([(beginWord, 1)])
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps

            for i in range(len_word):
                part1, part2 = word[:i], word[i + 1:]
                for c in range(ord('a'), ord('z') + 1):
                    if chr(c) != word[i]:
                        new_word = part1 + chr(c) + part2
                        if new_word in wordDict:
                            queue.append((new_word, steps + 1))
                            wordDict.remove(new_word)

        return 0

