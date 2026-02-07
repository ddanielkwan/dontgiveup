# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #use a window of size k
        #check how many vowels in that window

        l = 0

        maxVowels = 0 

        currentVowelsInWindow = 0

        for r in range(len(s)):

            if s[r] in "aeiuo":
                currentVowelsInWindow += 1 
            
            if r - l + 1 > k:
                if s[l] in "aeiou":
                    currentVowelsInWindow -= 1
                l += 1
            maxVowels = max(maxVowels, currentVowelsInWindow)
        
        return maxVowels


