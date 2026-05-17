# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #always keep the window valid grow it greedily shrink it only when invalid
        tracker = set()

        l = 0

        longest = 0
        for r in range(len(s)):

            while s[r] in tracker:
                tracker.remove(s[l])
                l += 1

            
            tracker.add(s[r])

            longest = max(longest, r - l + 1)
        
        return longest

