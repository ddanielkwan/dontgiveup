
# Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.

# If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

# For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
 

# Example 1:

# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.



class Trie:
    def __init__(self):
        self.children = {} #
        self.endoffolder = False

    def add(self, path):
        curr = self
        for f in path.split("/"):
            if f not in curr.children:
                curr.children[f] = Trie()
            curr = curr.children[f]
        curr.endoffolder= True


    def prefix_search(self, path):
        #idea: does this path have a parent folder already marked as complete?
        curr = self
        folders = path.split("/")
        for i in range(len(folders)-1):
            #cant look at last one why?
            curr = curr.children[folders[i]]
            if curr.endoffolder:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # #solu 1 hashste o(n * k^2) k slice k and k length word
        # folderSet = set(folder)

        # res = []


        # for f in folder:
        #     res.append(f)

        #     for i in range(len(f)):
        #         if f[i] == "/" and f[:i] in folderSet: #we ant all prefix before that slash /ab/ce -> /ab
        #             res.pop()
        #             break

        # return res
        # solu 2 : prefix trie

        trie = Trie()

        for f in folder:
            trie.add(f)

        res = []
        for f in folder:
            if not trie.prefix_search(f):
                res.append(f)

        return res
