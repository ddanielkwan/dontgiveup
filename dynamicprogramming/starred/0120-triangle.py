# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

# Example 1:

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
# Example 2:

# Input: triangle = [[-10]]
# Output: -10


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #What is the minimum sum to reach the bottom FROM this cell
        #bottom up

        # def dfs(row,col):
        #     if row >= len(triangle):
        #         return 0
        #     return triangle[row][col] + min(dfs(row+1, col),dfs(row+1,col+1))
        # return dfs(0,0)

        dp = [0] * (len(triangle)+1)

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                #this is top down
                #bottom row is 0 000 thts why + 1 trainagel
                dp[i] = n + min(dp[i], dp[i+1]) 
                #this index is pssible becase if you look from top, row 1 -> 0 index, row2 ->indices 0 and 1, since we do bottom up., btoom alwascalcualedfoirst
        return dp[0]

