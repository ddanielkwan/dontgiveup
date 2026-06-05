# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "(*)"
# Output: true


class Solution:
    def checkValidString(self, s: str) -> bool:

        memo = {}
        def dfs(i, open):
            if open < 0: # ()) we cant have more closed we cant recover
                return False

            if i == len(s):
                return open == 0 #perfect match is true

            if (i,open) in memo:
                return memo[(i, open)]
            if s[i] == '(':
                memo[(i, open)] = dfs(i + 1, open + 1)
                return memo[(i, open)]

            elif s[i] == ')':
                memo[(i, open)] = dfs(i + 1, open - 1)
                return memo[(i, open)]
            else:
                memo[(i,open ) ] = (dfs(i + 1, open) or
                        dfs(i + 1, open + 1) or
                        dfs(i + 1, open - 1))
                return memo[(i, open)]
        return dfs(0, 0)


class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            
            # # unmatched open parentheses can never be negative
# if leftMin < 0, it means we can use '*' as empty
# so the minimum possible unmatched opens becomes 0
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0