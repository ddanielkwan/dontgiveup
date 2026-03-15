# You are given a string s, 
# return the length of the longest substring that contains at most 
# two distinct characters.

# Note: A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:

# Input: s = "eceba"

# Output: 3
# Explanation: The substring is "ece" which its length is 3.

# Example 2:

# Input: s = "ccaabbb"

# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        tracker = {}

        l = 0

        longest = 0

        for r in range(len(s)):
            #add element first, fix window
            tracker[s[r]] = 1 + tracker.get(s[r], 0)

            #then determine validity 
            while len(tracker.keys()) > 2 :
                charLeft = s[l]
                tracker[charLeft] -= 1

                if tracker[charLeft] == 0:
                    del tracker[charLeft]

                l += 1
            #calculate result
            longest = max(longest, r - l + 1)
            
        
        return longest

