#SLIDING WINDOW
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #true if t is an anagram of s 

        stracker = [0] * 26
        ttracker = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            stracker[ord(s[i])- ord('a')]+=1
            ttracker[ord(t[i])-ord('a')] += 1
        
        return stracker==ttracker

