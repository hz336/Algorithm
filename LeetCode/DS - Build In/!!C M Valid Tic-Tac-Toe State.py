"""
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of
a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
"""


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        m, n = len(board), len(board[0])
        x_count, o_count = 0, 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    x_count += 1
                elif board[i][j] == 'O':
                    o_count += 1

        if x_count > o_count + 1 or x_count < o_count:
            return False

        if self.win(board, 'X') and self.win(board, 'O'):
            return False

        if self.win(board, 'X') and x_count != o_count + 1:
            return False

        if self.win(board, 'O') and x_count != o_count:
            return False

        return True

    def win(self, board, player):
        m, n = len(board), len(board[0])

        # Check row
        for i in range(m):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True

        # Check column
        for j in range(n):
            if board[0][j] == board[1][j] == board[2][j] == player:
                return True

        # Check Diagonal
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True

        if board[0][2] == board[1][1] == board[2][0] == player:
            return True

        return False
