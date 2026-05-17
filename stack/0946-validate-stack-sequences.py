# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

# Example 1:

# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1



class Solution:
    #s there any valid way a stack could pop elements to match popped, if I push in exactly the order of pushed
    # A stack can only pop the most recently pushed element
    # You don’t choose when to pop  you pop as soon as you’re allowed to
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:

        stack = []

        poppedIndex = 0
        for number in pushed:

            stack.append(number)

            while poppedIndex < len(popped) and stack and stack[-1] == popped[poppedIndex] :
                stack.pop()
                poppedIndex += 1
            
        
        return True if not stack else False


        

