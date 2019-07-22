"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.
"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) != 9 or len(board[0]) != 9:
            return 

        self.dfs(board)
        
    def dfs(self, board): 
        for i in range(9):
            for j in range(9): 
                if board[i][j] == '.': 
                    for c in range(1, 10): 
                        c = str(c)
                        if self.is_valid(board, i, j, c): 
                            board[i][j] = c
                            if self.dfs(board):
                                return True
                            else: 
                                board[i][j] = '.'
                                
                    return False
                
        return True                    
    
    def is_valid(self, board, row, col, c): 
        for i in range(9): 
            # check row
            if board[row][i] == c: 
                return False
            
            # check column
            if board[i][col] == c: 
                return False
            
            # check box
            if board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == c: 
                return False
            
        return True                        
                        
                        
                        
                        
                        
                        
                        
