# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #0 water
        #1 is land

        
        #exactly one island

        #out means we return one side perimeter
        visited = set() #to keep track of what square we visited so dont do again
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 1
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            res = 0

            directions = [[1,0],[-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                res += dfs(row, col)
            
            return res

            
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: #we only need to run dfs once since one island is connected
                    return dfs(r,c)