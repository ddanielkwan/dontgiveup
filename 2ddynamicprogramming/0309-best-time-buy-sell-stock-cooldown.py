# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        #intution: what is the state here
        #do nothing
        #buy, tjat means has to sell before buy again
        #sell, that means cooldown
        #first option is always buy

        #  # We're checking every decision at each day
        # prevbought == True → we already bought, we can sell
        # prevbought == False → we don't own a stock, so we can buy
        # When you buy a stock, your net profit decreases (you’re spending money)
        # When you sell a stock, your net profit increases (you’re earning money

        #caclualting the profti
        cache = {}

        def dfs(i, hasStock):
            if i >= len(prices):
                return 0
            
            if (i, hasStock) in cache:
                return cache[(i,hasStock)]
            #3 options
            idle = dfs(i+1, hasStock) #do nothing

            if not hasStock:
                #opt 2 : buy stock
                buy = dfs(i+1, True) - prices[i]
                cache[(i, hasStock)] = max(idle, buy)
                return cache[(i, hasStock)]
            else: 
                #i have stock now,
                # Option 2: Sell stock today (cooldown next day)
                #sell stock you must cooldown
                sell = dfs(i + 2, False) + prices[i] #When you sell on day i, day i+1 is frozen (cooldown). So the next day you can do anything is i+2

                cache[(i,hasStock)] = max(idle,sell)
                return  cache[(i,hasStock)]
        return dfs(0,False)
        

