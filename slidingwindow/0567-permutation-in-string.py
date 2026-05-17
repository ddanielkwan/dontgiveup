# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window, of size len(s1), once we find that window, compare the character frequencies array of both s1 and window , to see if equals
        
        if len(s2) < len(s1):
            return False #since if s2 is smaller, then s1 cannot be in s2
        
    
        s1Tracker = [0] * 26
        for n in s1:
            index = ord(n) - ord('a')
            s1Tracker[index] += 1

        s2Tracker = [0] * 26 

        l = 0
        
        for r in range(len(s2)):
            index = ord(s2[r]) - ord('a')

            s2Tracker[index] += 1
            #ou must fix the window first, then compare
            if r - l + 1 > len(s1):
                index = ord(s2[l]) - ord('a')
                s2Tracker[index] -= 1
                l += 1
          
            if s2Tracker == s1Tracker:
                return True
            
            
        
        return False
                



