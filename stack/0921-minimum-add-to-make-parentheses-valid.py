# A parentheses string is valid if and only if:

# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

 

# Example 1:

# Input: s = "())"
# Output: 1
# Example 2:

# Input: s = "((("
# Output: 3



class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        # Number of unmatched '(' seen so far
        openCount = 0

        # Number of parentheses we need to add
        minMoves = 0

        # Traverse the string character by character
        for c in s:

            # Opening parenthesis increases unmatched count
            if c == "(":
                openCount += 1

            else: #)
                # Closing parenthesis
                
                # If there is no '(' to match this ')'
                # we must add a '('
                if openCount == 0:
                    minMoves += 1
                else:
                    # Otherwise, match this ')' with an existing '('
                    openCount -= 1

        # any remaining '(' need ')' to be added
        return minMoves + openCount


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        # Stack to store unmatched parentheses
        # We only really care about '(' but using a stack
        # makes the logic very explicit and easy to reason about
        stack = []

        # Count how many parentheses we need to add
        minMoves = 0

        # Iterate through each character in the string
        for c in s:

            # If we see an opening parenthesis,
            # push it onto the stack to be matched later
            if c == "(":
                stack.append(c)

            else:
                # If we see a closing parenthesis ')'

                # Case 1: There is an unmatched '(' available
                # → pop it and form a valid "()"
                if stack:
                    stack.pop()

                # Case 2: No '(' available to match this ')'
                # -> we must ADD an opening '('
                else:
                    minMoves += 1

        # After processing the entire string,
        # any remaining '(' in the stack are unmatched
        # Each one needs a ')' to be added
        return minMoves + len(stack)
