# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution:
    def numSquares(self, n: int) -> int:

        # fill with n as "infinity" — worst case is n ones (1+1+1+...+1)
        # size n+1 because we need indexes 0 to n
        dp = [n] * (n + 1)
        
        # base case: 0 needs 0 squares to make it
        dp[0] = 0 
        
        # solve every subproblem from 1 up to n (bottom up)
        for target in range(1, n+1):
            
            # try every possible "last square" we could have used
            # s=1 → 1², s=2 → 4, s=3 → 9 ...
            for s in range(1, target+1):
                square = s * s
                
                # square is bigger than target, no point trying larger s
                # e.g. target=5, s=3 → square=9 > 5, stop
                if target - square < 0:
                    break
                
                # same as coin change:
                # "1 square I just used" + "best answer for the remainder"
                # e.g. target=12, square=4 → 1 + dp[8]
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        # answer for original n is fully built up
        return dp[n]

