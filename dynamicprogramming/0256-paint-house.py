# Description
# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. 
# The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, 
# and so on...
# Return the minimum cost to paint all houses.


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # n = len(costs)
        # cache = {}
        # def dfs(index, prevcolor):
        #     if index == n:
        #         return 0
        #     if (index,prevcolor) in cache:
        #         return cache[(index,prevcolor)]
            
        #     res = float('inf')
        #     for c in range(3):
        #         if c == prevcolor:
        #             continue
        #         res = min(res, costs[index][c] + dfs(index+1,c))
        #     cache[(index,prevcolor)] = res
        #     return res
        # return dfs(0,-1)
    

        #at every iteration we only care about the one before it
        # For the current house,
# we only need the minimum costs from the PREVIOUS house.
        dp = [0,0,0]
        for i in range(len(costs)):#every house
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0],dp[2])
            dp2 = costs[i][2] + min(dp[1],dp[0])
            dp = [dp0,dp1,dp2]
        return min(dp)

