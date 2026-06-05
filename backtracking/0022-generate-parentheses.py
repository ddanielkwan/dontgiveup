# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        substack = []

        def bt(opened, closed):

            if closed == opened == n :
                return res.append("".join(substack))
            
            if opened < n :
                substack.append("(")
                bt(opened+1,closed)
                substack.pop()
            
            if closed < n and closed < opened:
                substack.append(")")
                bt(opened, closed+1)
                substack.pop()
        
        bt(0,0)
        return res


