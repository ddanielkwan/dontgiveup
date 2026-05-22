# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5

class Solution:
    #tricky operation precedence 
    #we iterate through string, but dont do ddition or subtraction immediately, and push to stack, to see if higher precednece operator is coming
    # up next
    def calculate(self, s: str) -> int:
        #"3+2*2"
        #left to right
        #see 3 num = 3 
        #see + we know the preivous operation sohuld be applied

        #we wait for operator because we dont know what to do with that number unti lwe see the next operator   e.g
        #when reading 3, you dont know if 3+ , 3-, 3*, 3/
        stack = []
        num = 0
        op = '+'
        s = s.replace(' ', '')

        for i, ch in enumerate(s):
            if ch.isdigit(): #to build multi digit "123" 
                num = num * 10 + int(ch)
            if (not ch.isdigit()) or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)#treat whateveris in stack as what we want to add

                elif op == '*':
                    stack.append(stack.pop() * num)

                else:
                    prev = stack.pop()
                    stack.append(int(prev / num))
                op = ch
                num = 0

        return sum(stack)

