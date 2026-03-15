# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

from collections import Counter


#COUTNTER HASHMAP
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        balloon = Counter("balloon")

        t = Counter(text)

        res = len(text)

        for char in balloon:
            res = min(res,t[char]//balloon[char])
            
        return res
    