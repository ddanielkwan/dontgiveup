# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string],
#  where the encoded_string inside the square brackets is being repeated exactly k times.
#  Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid;
#  there are no extra white spaces, square brackets are well-formed, etc. 
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
# For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"

class Solution:
    def decodeString(self, s: str) -> str:
        #we have to process the latest one we see
        #so we need to use a stack
        #e.g 3[a2[c]] we see 3 so we go inside, but we see 2, so we have to go inside again
        #suddenly we see ] this means we need to start processing what we had before and append to stack


        stack = []

        for character in s:
            if character == "]":
                pattern = ""
                while stack and stack[-1] != "[":
                    alphabet = stack.pop()
                    pattern = alphabet + pattern #add in front
                
                #now we found the pattern lets make sure to remove "["
                stack.pop()

                #next step is to find the number of times the pattern repeats, so the integer
                repeat = ""
                while stack and stack[-1].isdigit():
                    repeat = stack.pop() + repeat
                
                repeat = int(repeat) #turn to int
                
                #add back to stack
                stack.append(repeat * pattern) 
            else:
                stack.append(character)
        
        return "".join(stack)


