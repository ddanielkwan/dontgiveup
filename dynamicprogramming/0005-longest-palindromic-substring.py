# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0

        for i in range(len(s)):
            #Odd length
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r - l + 1
                if curLen > maxLen:
                    maxLen = curLen
                    res = s[l:r+1]
                l-=1
                r+=1
            #Even length
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curLen = r - l + 1
                if curLen > maxLen:
                    maxLen = curLen
                    res = s[l:r+1]
                l-=1
                r+=1
        return res

