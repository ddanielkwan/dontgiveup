# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.


from collections import defaultdict

#use HASHMAP to store anagrams, need to decide on common key 
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagrams = defaultdict(list)

        #we can use a hashmap to store all the words which are anagrams of x (key)
        #this key, since we are working with alphabetical we can use 26 elements of array and
        #get the count of each character

        for word in strs:
            key = [0] * 26 

            for character in word:
                keyIndex = ord(character) - ord("a")
                key[keyIndex] += 1

            #have to use tuple because it is immutable, hashmaps only allow for immutable key 
            anagrams[tuple(key)].append(word)

        return list(anagrams.values())





        
        