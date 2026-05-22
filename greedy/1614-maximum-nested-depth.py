# Given a valid parentheses string s, return the nesting depth of s. 
# The nesting depth is the maximum number of nested parentheses.

 

# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"

# Output: 3

# Explanation:

# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:

# Input: s = "(1)+((2))+(((3)))"

# Output: 3

# Explanation:

# Digit 3 is inside of 3 nested parentheses in the string.

class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        res = 0
        for c in s:
            if c == "(":
                count += 1
                res = max(res,count)
            elif c == ")" : 
                count -= 1
        return res
    