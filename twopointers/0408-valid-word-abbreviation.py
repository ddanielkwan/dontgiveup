# A string can be shortened by replacing any number of non-adjacent, non-empty substrings with their lengths (without leading zeros).

# For example, the string "implementation" can be abbreviated in several ways, such as:

# "i12n" -> ("i mplementatio n")
# "imp4n5n" -> ("imp leme n tatio n")
# "14" -> ("implementation")
# "implemetation" -> (no substrings replaced)
# Invalid abbreviations include:

# "i57n" -> (i mplem entatio n, adjacent substrings are replaced.)
# "i012n" -> (has leading zeros)
# "i0mplementation" (replaces an empty substring)
# You are given a string named word and an abbreviation named abbr, return true if abbr correctly abbreviates word, otherwise return false.

# A substring is a contiguous non-empty sequence of characters within a string.

# Example 1:

# Input: word = "apple", abbr = "a3e"

# Output: true
# Example 2:

# Input: word = "international", abbr = "i9l"

# Output: false

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        #intuition: if see numbers, skip that many lengths, so we need two pointers
    
        n = len(word)
        m = len(abbr)

        i = 0
        j = 0

        while i < n and j < m :
            if abbr[j] == '0':
                return False

            if word[i] == abbr[j]:
                i += 1
                j += 1
            
            elif abbr[j].isalpha(): #not equals and is alphabet
                return False
            
            else: #abbr[j] is a digit and we need to find digit 
                length = 0
                while j < m and abbr[j].isdigit():
                    length = length * 10 + int(abbr[j])
                    j += 1
                
                i += length
        
        return i == n and j == m
