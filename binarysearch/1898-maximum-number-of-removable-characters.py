# You are given two strings s and p where p is a subsequence of s. 
# You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

# You want to choose an integer k (0 <= k <= removable.length) such that,
#  after removing k characters from s using the first k indices in removable, p is still a subsequence of s.
#  More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters 
# and check if p is still a subsequence.

# Return the maximum k you can choose such that p is still a subsequence of s after the removals.

# A subsequence of a string is a new string generated from the original string with some characters (can be none)
#  deleted without changing the relative order of the remaining characters.

 

# Example 1:

# Input: s = "abcacb", p = "ab", removable = [3,1,0]
# Output: 2
# Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
# "ab" is a subsequence of "accb".
# If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
# Hence, the maximum k is 2.


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        

        #hint: it says find 0 <= k < removable
        #usually is binary search
        #do binary search and check how many elemnets you can remove thats stilll subsequence

        def stillSubsequence(s, subseq, removed): #o(s)
            i1 = 0
            i2 = 0

            while i1 < len(s) and i2 < len(subseq):
                if i1 in removed or s[i1] != subseq[i2]:
                    i1 += 1
                    continue
                i1 += 1
                i2 += 1
            
            return i2 == len(subseq)

        

        res = 0
        l = 0
        r = len(removable) - 1 

        while l <= r : # o(logr)
            m = (l+r)//2 
            #o(m) slciing
            removed = set(removable[:m+1]) #get k removable indices

            if stillSubsequence(s, p , removed):
                res = max(res, m + 1)
                l = m + 1
            else:
                r = m - 1
        
        return res

