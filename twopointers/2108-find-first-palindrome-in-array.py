# Given an array of strings words, return the first palindromic string in the array. 
# If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

 

# Example 1:

# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.


class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        
        def ispalindrome(word,l,r):
            while l < r :
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for word in words:
            if ispalindrome(word, 0, len(word)-1):
                return word
        return ""