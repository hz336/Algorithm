"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example
Given board =

[
  "ABCE",
  "SFCS",
  "ADEE"
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """

    def exist(self, board, word):
        # write your code here
        if word == "":
            return True

        m = len(board)
        n = len(board[0])
        if m == 0 or n == 0:
            return False

        visited = [[False for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                find = self.dfs(board, word, 0, row, col, visited)
                if find:
                    return True

        return False

    def dfs(self, board, word, index, row, col, visited):
        if index == len(word):
            return True

        m = len(board)
        n = len(board[0])
        if row < 0 or row >= m or col < 0 or col >= n:
            return False

        if board[row][col] == word[index] and not visited[row][col]:
            visited[row][col] = True
            find = self.dfs(board, word, index + 1, row + 1, col, visited) | \
                   self.dfs(board, word, index + 1, row - 1, col, visited) | \
                   self.dfs(board, word, index + 1, row, col + 1, visited) | \
                   self.dfs(board, word, index + 1, row, col - 1, visited)

            if find:
                return True

            visited[row][col] = False

        return False


