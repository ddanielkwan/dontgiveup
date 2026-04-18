# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:

# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def dfs(i, j):
            if i < 0 or j == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == s[j]:
                length = 1 if i == j else 2
                dp[i][j] = length + dfs(i - 1, j + 1)
            else:
                dp[i][j] = max(dfs(i - 1, j), dfs(i, j + 1)) #we can skip character
            
            return dp[i][j]

        for i in range(n):
            dfs(i, i)  # odd length
            dfs(i, i + 1)  # even length
        
        return max(max(row) for row in dp if row != -1)