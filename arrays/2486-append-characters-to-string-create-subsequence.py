# You are given two strings s and t consisting of only lowercase English letters.

# Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        #let's use a pointer on T, where the pointer stops we can calculate how many characters we need to add
        #after we finished traversing S

        tpointer = 0

        for i in range(len(s)):
            if s[i] == t[tpointer]:
                tpointer += 1
                
            if tpointer == len(t):
                return 0
        
        return len(t) - tpointer

