
# Topics
# conpanies icon
# Companies
# Hint
# Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

# If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

# Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

 

# Example 1:

# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".



# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         # Key Insight: A word can be built one character at a time only if every prefix of that word also exists in words

#         #solu 1 

#         word_set = set(words)
#         # sort by length, then lexicographically for ties
#         words.sort(key=lambda x: (len(x), x))
        
#         result = ""
#         # O(n log n + n × L²) 
#         for word in words:
#             # every prefix must exist in the set
#             if all(word[:i] in word_set for i in range(1, len(word))):
#                 if len(word) > len(result):
#                     result = word
        
        # return result


class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
        self.word = ""

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.eow = True
            node.word = word

        self.result = ""

        def dfs(node):
            for child in node.children.values():
                if child.eow: #we can only go if child is eow
                    if len(child.word) > len(self.result) or (len(child.word) == len(self.result) and child.word < self.result):
                        self.result = child.word
                    dfs(child)  # only recurse if valid word end

        dfs(root)
        return self.result

