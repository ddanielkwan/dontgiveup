# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]


class Solution:
    #use the count of each word seperated by deliminter
    def encode(self, strs: list[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> list[str]:

        index = 0

        res = []

        while index < len(s):
            j = index

            while s[j] != "#": #get the integer part
                j += 1
            
            lengthOfWord = s[index:j]

            index = j

            word = s[index + 1: index + lengthOfWord +1]
            index = index + lengthOfWord + 1
            res.append(word)

        return res

