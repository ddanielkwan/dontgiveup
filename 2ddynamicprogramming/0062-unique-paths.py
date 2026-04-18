# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 


# O(n*m)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows = m
        cols = n

        # +1 padding on each dimension so we can safely access dp[r+1] and dp[c+1]
        # without index-out-of-bounds at the last row/col — the extra row/col stays 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Base case: there is exactly 1 path when you're already at the destination
        dp[m-1][n-1] = 1

        # Traverse bottom-up, right-to-left so that when we compute dp[r][c],
        # dp[r+1][c] (down) and dp[r][c+1] (right) are already filled in
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                
                # Skip the destination — its value is already set to 1 above
                if r == m - 1 and c == n - 1:  
                    continue
                
                # Number of paths from (r,c) = paths going down + paths going right
                # dp[r+1][c] → one step down
                # dp[r][c+1] → one step right
                # Out-of-bounds neighbors are 0 thanks to the padding row/col
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        
        # The answer is the number of paths from the top-left corner
        return dp[0][0]