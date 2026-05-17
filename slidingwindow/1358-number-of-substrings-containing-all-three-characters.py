# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 


from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # abc
        # abca
        # abcab
        # abcabc
        # bca
        # bcab
        # bcabc
        # cab
        # cabc
        # abc

        #how to use window here
        #note the minimum window we must have is of size 3 because it must contain abc
        #also take a look at 
        #abcaab if we have window abc, then that means we also have abca abcaa abcaab beacause abc is already valid so we len(s) - r = 4
        
        l = 0
        res = 0

        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1

            while len(count) == 3:
                res += len(s) - r
                count[s[l]] -= 1

                if count[s[l]] == 0:
                    del count[s[l]]
                
                l += 1
        return res

