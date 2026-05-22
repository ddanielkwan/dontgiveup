# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
# - WordDictionary() Initializes the object.
# - void addWord(word) Adds word to the data structure, it can be matched later.
# - bool search(word) Returns true if there is any string in the data structure that matches word,
#   otherwise return false. word may contain dots '.' where dots can be matched with any letter.

# Example 1:
# Input: ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
#        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output: [null,null,null,null,false,true,true,true]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # standard trie insert
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        # use dfs to handle '.' wildcard
        def dfs(index, node):
            if index == len(word): #return true if is end
                return node.is_end

            char = word[index]

            if char == '.': #this is current, so we dont care whre we are now, if any of our children is true
                #return true
                # '.' matches any character — try all children
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])

        return dfs(0, self.root)

