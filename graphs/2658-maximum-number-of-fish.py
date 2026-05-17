# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

# A land cell if grid[r][c] = 0, or
# A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations any number of times:

# Catch all the fish at cell (r, c), or
# Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

# Example 1:


# Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
# Output: 7
# Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        #grid(r,c) is 0 land or water if > 0

        #start anywhere

        #catch all fish at cell (rc)
        #or move to any adjacent water cell

        #return maxiumum fish the fisher can ctch if start cell is optimal
        rows = len(grid)
        cols = len(grid[0])
        maxFish = 0
        visited = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            res = grid[r][c]

            res += dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            return res


        for r in range(rows):
            for c in range(cols):
                maxFish = max(maxFish, dfs(r,c))
        
        return maxFish

