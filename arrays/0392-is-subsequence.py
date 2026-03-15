# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


#USE TWO POINTER
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #is S a sub seq of T
        #have a pointer on the s element once pointer is >= len of s, then means we successfully found every single char in t
        spointer = 0
        
        if s == "":
            return True
        
        if len(s) > len(t):
            return False
        
        for i in range(len(t)):
            if t[i] == s[spointer]:
                spointer += 1
                if spointer == len(s):
                    return True
        return False
        