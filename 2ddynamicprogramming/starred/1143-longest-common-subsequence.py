# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none)
#  deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        rows = len(text1)
        cols = len(text2)

        dp = [[0] * (cols+1) for _ in range(rows+1)]
        #idea

        #abcde
        #ace

        #subproblem is 
        #bcde vs 
        #ce

        #or 
        #
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if text1[r] == text2[c]:
                    dp[r][c] = dp[r+1][c+1] + 1
                else:
                    # This line handles the case where characters don't match. Since they don't match, you have to skip one character from one of the strings. You try both options and take the better one
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])
        
        return dp[0][0]

