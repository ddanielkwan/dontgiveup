# You are given two strings s and t of the same length and an integer maxCost.

# You want to change s to t. 
# Changing the ith character of s to ith character of t costs |s[i] - t[i]|
#  (i.e., the absolute difference between the ASCII values of the characters).

# Return the maximum length of a substring of s
#  that can be changed to be the same as the corresponding
#  substring of t with a cost less than or equal to maxCost.
#  If there is no substring from s that can be changed to its corresponding substring from t, return 0.

 

# Example 1:

# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd".
# That costs 3, so the maximum length is 3.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        

        l = 0

        maxLength = 0

        currentCost = 0

        for r in range(len(s)):
            if s[r] != t[r]:
                currentCost += abs(ord(s[r])-ord(t[r]))

            while currentCost > maxCost:
                currentCost -= abs(ord(s[l])-ord(t[l]))
                l += 1
            
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength


