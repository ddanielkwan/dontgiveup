# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #intuition: wouldn't the digits near the front be the largest? so shouldnt we remove those?
        #can we have an increasing stack 
        #digits closer to the front matter more than digits later
        #removing a larger digit on the left reduces the number more than removing one on the right
        #if a digit is greater than the digit that comes after it, keeping it is bad for us

        stack = []

        for char in num:
            #makes sense to pop the one greater,. the ones at front
            while stack and stack[-1] > char and k > 0:
                stack.pop()
                k -= 1
            
            stack.append(char)
        
        #edge case: "3" k = 1, single char
        while stack and k:
            stack.pop()
            k -= 1
        
        #case where stack ends up starting with "0" -> [0200]
        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1
        stack = stack[i:]
        print(stack)
        #case where num = "10" k = 2, stack will be empty
        return "".join(stack) if stack else "0"

