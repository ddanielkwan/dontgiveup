# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:


# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return 0 #not possible to start or end
        
        dp= [[0] * (cols+1) for _ in range(rows+1)]

        dp[rows-1][cols-1] = 1

        for r in range(rows-1, -1, -1):
            for c in range(cols-1,-1,-1):
                if r == rows-1 and c == cols-1:
                    continue
                if grid[r][c] == 1:
                    continue
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]