# You are given a string s and an integer k, 
# a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them,
#  causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #intuition: The key phrase in the problem is:
        # k adjacent and equal letters
        # and after removal, the left and right sides concatenate
        # That tells us two things:
        # Adjacency matters
        # New adjacencies can be created after deletions
        # This is exactly the kind of problem where a stack shines

        #can we store the count and character in the stack?
        #(char, count)
        #keeping track of the character and count, [char1,2] [char2,1]
        #we just change the last element of stack and update the count
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1] = (char, stack[-1][1] + 1)

                if stack and stack[-1][1] == k:
                    stack.pop()
            
            else:
                stack.append((char, 1))
        
        finalString = ""

        for char, count in stack:
            finalString += char * count
        
        return finalString




