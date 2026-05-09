# You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1> and <num2> represent positive integers.

# Add a pair of parentheses to expression such that after the addition of parentheses, expression is a valid mathematical expression and evaluates to the smallest possible value. The left parenthesis must be added to the left of '+' and the right parenthesis must be added to the right of '+'.

# Return expression after adding a pair of parentheses such that expression evaluates to the smallest possible value. If there are multiple answers that yield the same result, return any of them.

# The input has been generated such that the original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

 

# Example 1:

# Input: expression = "247+38"
# Output: "2(47+38)"
# Explanation: The expression evaluates to 2 * (47 + 38) = 2 * 85 = 170.
# Note that "2(4)7+38" is invalid because the right parenthesis must be to the right of the '+'.
# It can be shown that 170 is the smallest possible value.




class Solution:
    def minimizeResult(self, expression: str) -> str:
        # a(b+c)d  =  a*b*d + a*c*d

        #brute force try every possible split

        plus = expression.index('+')
        num1 = expression[:plus]
        num2 = expression[plus+1:]
        
        best_val = float('inf')
        best_expr = ""
        
        # i splits num1 into num1[:i] and num1[i:]
        for i in range(len(num1)):
            # j splits num2 into num2[:j+1] and num2[j+1:]
            for j in range(len(num2)):
                a = int(num1[:i]) if num1[:i] else 1
                b = int(num1[i:])
                c = int(num2[:j+1])
                d = int(num2[j+1:]) if num2[j+1:] else 1
                
                val = a * (b + c) * d
                
                if val < best_val:
                    best_val = val
                    best_expr = num1[:i] + "(" + num1[i:] + "+" + num2[:j+1] + ")" + num2[j+1:]
        
        return best_expr