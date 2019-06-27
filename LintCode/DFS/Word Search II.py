"""
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any
position in the matrix and go left/right/up/down to the adjacent position.

Example
Given matrix:

doaf
agai
dcan

and dictionary:
{"dog", "dad", "dgdg", "can", "again"}

return {"dog", "dad", "can", "again"}
"""


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        # write your code here
        if words is None or len(words) == 0:
            return []

        m = len(board)
        n = len(board[0])
        if m == 0 or n == 0:
            return []

        prefix_set = self.get_prefix_set(words)
        print(prefix_set)

        visited = [[False for _ in range(n)] for _ in range(m)]
        results = []
        for row in range(m):
            for col in range(n):
                visited[row][col] = True
                self.dfs(board, visited, row, col, board[row][col], prefix_set, results)
                visited[row][col] = False

        return results

    def get_prefix_set(self, words):
        prefix_set = {}
        for word in words:
            for i in range(len(word) - 1):
                prefix = word[: i + 1]
                if prefix not in prefix_set:
                    prefix_set[prefix] = False

            prefix_set[word] = True

        return prefix_set

    def dfs(self, board, visited, x, y, word, prefix_set, results):
        if word not in prefix_set:
            return

        if prefix_set[word] and word not in results:
            results.append(word)

        x_delta = [-1, 1, 0, 0]
        y_delta = [0, 0, -1, 1]
        for i in range(4):
            new_x = x + x_delta[i]
            new_y = y + y_delta[i]
            if not self.is_valid(board, new_x, new_y) or visited[new_x][new_y]:
                continue

            visited[new_x][new_y] = True
            self.dfs(board, visited, new_x, new_y, word + board[new_x][new_y], prefix_set, results)
            visited[new_x][new_y] = False

    def is_valid(self, board, x, y):
        m = len(board)
        n = len(board[0])
        return 0 <= x < m and 0 <= y < n

