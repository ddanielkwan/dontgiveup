# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

 

# Example 1:

# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        
        #we will need four pointers
        #intution : don’t care about the words
        # only care about the sequence of characters they produce

        word1Pointer = 0
        word2Pointer = 0

        wi = 0
        wj = 0

        while word1Pointer < len(word1) and word2Pointer < len(word2):
            charOne = word1[word1Pointer][wi]
            charTwo = word2[word2Pointer][wj]

            if charOne != charTwo :
                return False
            
            wi += 1
            wj += 1

            if wi == len(word1[word1Pointer]):
                wi = 0
                word1Pointer += 1
            
            if wj == len(word2[word2Pointer]):
                wj = 0
                word2Pointer += 1
            
        return True if word1Pointer == len(word1) and word2Pointer == len(word2) else False




