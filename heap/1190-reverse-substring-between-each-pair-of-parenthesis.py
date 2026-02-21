# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

 

# Example 1:

# Input: s = "(abcd)"
# Output: "dcba"
# Example 2:

# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.

class Solution:
    def reverseParentheses(self, s: str) -> str:
        #some portiosn of string can get revsersed multiple times

        #solu 1 use stack
        # stack = []


        # for c in s:
        #     if c == ")":
        #         portion = []
        #         while stack[-1] != "(":
        #             portion.append(stack.pop()) #this is reversing already
        #         stack.pop()
        #         stack.extend(portion)
            
        #     else:
        #         stack.append(c)
        
        # return "".join(stack)

        # solution 2 heap
        #note, the outer portion gets reversed once, while inner may reverse 2,3,4... etc.
        #anytime we see parentesis, we will automaticallhy go to the other one and look from that side iteratively

        direction =  1
        res = []
        pairs = {}
        #preprocessing to compiute all matching pairs and get where the oppsite bracket is for complete bracet pair
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                j = stack.pop()
                pairs[j] = i
                pairs[i] = j
        i = 0
        while i < len(s):
            if s[i] == "(" or s[i] == ")":
                i = pairs[i]
                direction = -1 * direction

            else:
                res.append(s[i])
            i += direction 
        return "".join(res)

