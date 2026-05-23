# Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

# Example 1:

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# Example 2:

# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
 

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        #can we use a sliding window here
        #a valid window is if distinct characters in this window <= k
        #invalid is if distinct fcharactesr > k
        #how to keep track of distinct characters? we can use a freq hashmap

        #if window is invalid, we need to remove elemnets from left side until vaid

        freq = defaultdict(int)

        l = 0

        maxLength = 0

        for r in range(len(s)):
            freq[s[r]] += 1

            while len(freq) > k: #invalid
                #shrink it
                charLeft = s[l]
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            
            maxLength = max(maxLength, r-l+1)
        
        return maxLength