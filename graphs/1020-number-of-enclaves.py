# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

# Example 1:


# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        #1 is land

        #just dfs on the edges and turn all 1s touching to 0s then for loop to count 1s
        visited = set()
        def dfs(r,c):
            if r < 0 or r >=rows or c < 0 or c>=cols or (r,c) in visited or grid[r][c] == 0:
                return
            
            visited.add((r,c))
            grid[r][c] = 0 #set as 0 since touching edge
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            if grid[r][0] == 1:
                dfs(r,0)
            if grid[r][cols-1] == 1:
                dfs(r,cols-1)
        
        for c in range(cols):
            if grid[0][c] == 1:
                dfs(0,c)
            if grid[rows-1][c] == 1:
                dfs(rows-1,c)
        
        #remaining is what not touching edge
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res += 1
        
        return res
            

