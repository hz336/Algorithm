"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill
using one bomb. The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall 
is too strong to be destroyed.

Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
"""

"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        m, n = len(grid), len(grid[0])
        up = [[0 for _ in range(n)] for _ in range(m)]
        down = [[0 for _ in range(n)] for _ in range(m)]
        left = [[0 for _ in range(n)] for _ in range(m)]
        right = [[0 for _ in range(n)] for _ in range(m)]
        
        # up 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W': 
                    continue
                
                if grid[i][j] == 'E':
                    up[i][j] = 1

                if i != 0: 
                    up[i][j] += up[i - 1][j]
        
        # down 
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if grid[i][j] == 'W': 
                    continue
                
                if grid[i][j] == 'E':
                    down[i][j] = 1
                    
                if i != m - 1:
                    down[i][j] += down[i + 1][j]
        
        # left
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W': 
                    continue
                
                if grid[i][j] == 'E':
                    left[i][j] = 1
                    
                if j != 0: 
                    left[i][j] += left[i][j - 1]
        
        # right 
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 'W': 
                    continue
                
                if grid[i][j] == 'E':
                    right[i][j] = 1
                    
                if j != n - 1:
                    right[i][j] += right[i][j + 1]
       
        # maximum
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    result = max(result, up[i][j] + down[i][j] + left[i][j] + right[i][j])
        
        return result
    
        
        
        
        
        
      
