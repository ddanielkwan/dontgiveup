# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

#USE HASHSET
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        #if we can map one character from s to t, we can also map one character from t to s
        #if s to t does not match t to s, then there is an issue 

        sToT = {}
        tToS = {}

        #the words have to be equal for us to even compare
        if len(s) != len(t):
            return False
        
        for index, charS in enumerate(s):

            charT = t[index]

            if charS in sToT and sToT[charS] != charT:
                return False
            
            if charT in tToS and tToS[charT] != charS:
                return False

            sToT[charS] = charT
            tToS[charT] = charS
        
        return True


