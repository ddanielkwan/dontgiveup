# A substring is a contiguous (non-empty) sequence of characters within a string.

# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

# Given a string word, return the number of vowel substrings in word.

 

# Example 1:

# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        res = 0

        for i in range(len(word)):
            seen = set()

            for j in range(i, len(word)):
                # stop if consonant
                if word[j] not in vowels:
                    break

                seen.add(word[j])

                # all 5 vowels present
                if len(seen) == 5:
                    res += 1

        return res