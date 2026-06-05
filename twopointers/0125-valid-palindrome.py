# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
#  it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isPaliRecursive(self,s, l: int, r: int):
              s.replace(', :', "")

        #recursively
        return self.isPaliRecursive(s,0 ,len(s)-1)

    #base case for recursion, is if the index we are comparing from left side and right side is same]
    #this means we start base case from middle, means we made it all theway to middle and non of those character are mismatch
    def isPaliRecursive(self,s, l: int, r: int):

        if l == r:
            return True

        if s[l] != s[r]:
            return False

       
        if l < r + 1:
            return self.isPaliRecursive(s, l+1, r-1)
        
        return True

