# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"

# Output: true

# Explanation:

# The bijection can be established as:

# 'a' maps to "dog".
# 'b' maps to "cat".
from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words)!=len(pattern):
            return False

        wordToPattern = defaultdict(str)
        patternToWord = defaultdict(str)

        for i in range(len(words)):
            pat = pattern[i]

            if pat in patternToWord and patternToWord[pat] != words[i]:
                return False
            if words[i] in wordToPattern and wordToPattern[words[i]] != pat:
                return False
            
            patternToWord[pat] = words[i]
            wordToPattern[words[i]] = pat
        return True
            
            