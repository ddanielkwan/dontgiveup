# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #go through all cells, if 1 and then add to count, then dfs starting from that cell and change all to 0 as visited so we dont reprocess
        
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        numberOfIslands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    numberOfIslands += 1
                    dfs(r,c)
        
        return numberOfIslands

