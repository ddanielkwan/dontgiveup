# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # we will have two pointers, one pointer points to start index of wordone and another for start index for wordtwo
        # to alternate, we take turns appending the character at each pointer to the new string
        # we want to ensure that the remaining gets appended, e.g one word longer than other abc vs defgh -> adbecf gh

        pointerOne = 0
        pointerTwo = 0

        mergedString = ""


        while pointerOne < len(word1) and pointerTwo < len(word2):

            mergedString = mergedString +  word1[pointerOne] + word2[pointerTwo]
            pointerOne += 1
            pointerTwo += 1
        

        if pointerOne < len(word1): #remaining
            mergedString += word1[pointerOne:]
        
        if pointerTwo < len(word2):
            mergedString += word2[pointerTwo:]
        
        return mergedString

            

        
