# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
 


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        #inition min_cost(r, c) = grid[r][c] + min(min_cost(r-1, c), min_cost(r, c-1))
        #memo
        cache = {}
        def dfs(r,c):

            if r >= rows or c >= cols:
                return float("inf")
            
            if (r,c) in cache:
                return cache[(r,c)]
            
            if r == rows - 1 and c == cols-1:
                return grid[r][c]
            cache[(r,c)] = grid[r][c] + min(dfs(r+1,c), dfs(r,c+1))
            return cache[(r,c)]
        
        return dfs(0,0)

