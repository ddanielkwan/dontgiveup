# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

 

# Example 1:

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:

# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:

# Input: amount = 10, coins = [10]
# Output: 1


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #The core insight is: process one coin at a time, and for each coin, update how many ways you can form every amount.

        # coin and amount is key

        #if you think of tree, how to ensure no duplicates
        #e.g [1,2,5] -> tree go down path 1,2,2
        #e.g tree go down path 2,2,1 <- duplicate
        #we can start by seeing combinations that start at 1
        #then go to 2 and do not alloow for 1 to be added

        # cache = {}
        # def dfs(index, amount):
        #     if amount == 0:
        #         return 1
            
        #     if index >= len(coins):
        #         return 0
            
        #     if (index,amount) in cache:
        #         return cache[(index,amount)]
            
        #     #option 1 : skip current coin
        #     res = dfs(index+1, amount) #do nothing

        #     #option 2 :use current coint (unlimited)
        #     if amount >= coins[index]:
        #         res += dfs(index, amount - coins[index])
            
        #     cache[(index,amount)] = res
        #     return res
        # return dfs(0, amount)


#         coins = [1, 2, 5] (after sort), amount = 5

#        a=0  a=1  a=2  a=3  a=4  a=5
# i=0  [  1,   1,   2,   2,   3,   4  ]  ← using coins [1,2,5]  → ANSWER
# i=1  [  1,   0,   1,   0,   1,   1  ]  ← using coins [2,5]
# i=2  [  1,   0,   0,   0,   0,   1  ]  ← using coins [5]
# i=3  [  1,   0,   0,   0,   0,   0  ]  ← using NO coins (base case)
        n = len(coins)
        coins.sort()

        #i is amount the second dimension is index?
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a] #skip this coin number of combinations if skip
                    dp[i][a] += dp[i][a - coins[i]] #number of combinations if not skip

        return dp[0][amount]

