# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

# Return the maximum amount of gold you can collect under the conditions:

# Every time you are located in a cell you will collect all the gold in that cell.
# From your position, you can walk one step to the left, right, up, or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.
 

# Example 1:

# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or c >= cols or r >= rows or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            max_gold = 0
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr , dc in directions:
                row = r + dr
                col = c + dc
                max_gold = max(max_gold, dfs(row,col))
            
            visited.remove((r,c))
            return max_gold + grid[r][c]

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    res = max(res,dfs(r,c))
        
        return res

