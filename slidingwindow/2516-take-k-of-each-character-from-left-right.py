# You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. 
# Each minute, you may take either the leftmost character of s, or the rightmost character of s.

# Return the minimum number of minutes needed for you to take at least k of each character,
#  or return -1 if it is not possible to take k of each character.

 

# Example 1:

# Input: s = "aabaaaacaabc", k = 2
# Output: 8
# Explanation: 
# Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
# Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
# A total of 3 + 5 = 8 minutes is needed.
# It can be proven that 8 is the minimum number of minutes needed.


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
       

        counts = [0,0,0]
        
        for c in s:
            counts[ord(c) - ord('a')] += 1
        if min(counts) < k:
            return -1
        #makeinner window as big as i can as long as a b and c are all > k=

        l = 0
        #usually we add , but this time, we would dtake away 
        res = float('inf')
        for r in range(len(s)):
            counts[ord(s[r])- ord('a')] -= 1

            while min(counts) < k :
                counts[ord(s[l])-ord('a')] += 1
                l += 1
            res = min(res, len(s) - (r-l+1)) #basically max of(windowsize) r-l+1
        
        return res

