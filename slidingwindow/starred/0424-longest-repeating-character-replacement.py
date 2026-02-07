# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #use a hashmap to keep track of highesst frequency and if current window - maxfreq char is <= k we can continue

        count = {}

        longest = 0

        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            #while window now valid
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #use a hashmap to keep track of highesst frequency and if current window - maxfreq char is <= k we can continue

        count = {}

        longest = 0

        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            #while window now valid, rather than calculating max everytime, just keep max pointer
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest

