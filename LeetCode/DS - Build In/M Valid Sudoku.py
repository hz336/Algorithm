"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""

"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if board is None or len(board) != 9 or len(board[0]) != 9:
            return False
        
        m, n = len(board), len(board[0])
        
        # Check row
        for i in range(m):
            row_check = {}
            for j in range(n):
                if board[i][j] == '.':
                    continue 
                
                if board[i][j] not in row_check:
                    row_check[board[i][j]] = 1
                else: 
                    return False
            
        # Check column
        for j in range(n):
            col_check = {}
            for i in range(m):
                if board[i][j] == '.':
                    continue 

                if board[i][j] not in col_check:
                    col_check[board[i][j]] = 1
                else: 
                    return False
        
        # Check 3 x 3
        for i in range(0, m, 3):
            for j in range(0, n, 3):
                box_check = {}
                for x in range(3):
                    for y in range(3):
                        if board[i + x][j + y] == '.':
                            continue
                            
                        if board[i + x][j + y] not in box_check:
                            box_check[board[i + x][j + y]] = 1
                        else: 
                            return False
                                
        return True
    
        
        
        
        
        
        
