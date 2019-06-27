"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False

        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if self.is_valid(board, row, col, visited, word[0]) and self.dfs(word, board, row, col, visited, 0):
                    return True

        return False

    def dfs(self, word, board, row, col, visited, index):
        if index == len(word):
            return True

        if not self.is_valid(board, row, col, visited, word[index]):
            return False

        visited[row][col] = True
        if self.dfs(word, board, row - 1, col, visited, index + 1) or \
                self.dfs(word, board, row + 1, col, visited, index + 1) or \
                self.dfs(word, board, row, col - 1, visited, index + 1) or \
                self.dfs(word, board, row, col + 1, visited, index + 1):
            return True
        visited[row][col] = False

        return False

    def is_valid(self, board, x, y, visited, c):
        m, n = len(board), len(board[0])
        return 0 <= x < m and 0 <= y < n and board[x][y] == c and not visited[x][y]
