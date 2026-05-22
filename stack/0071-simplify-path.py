# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'.
#  Your task is to transform this absolute path into its simplified canonical path.

# The rules of a Unix-style file system are as follows:

# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a 
# valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:

# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

 

# Example 1:

# Input: path = "/home/"

# Output: "/home"

# Explanation:

# The trailing slash should be removed.

# Example 2:

# Input: path = "/home//foo/"

# Output: "/home/foo"

# Explanation:

# Multiple consecutive slashes are replaced by a single one.


class Solution:
    def simplifyPath(self, path: str) -> str:
        #always begins with "/"
        #// or ///// treated as /
        #path start with /
        #directories seperated by /
        #cant end with / unless root
        #no single or double

        path = path.split("/")
        print(path)

        stack = []

        for item in path:
            if item == "." or item == "": #current directory does nothing
                continue
            
            elif item == "..":
                if stack:
                    stack.pop() #we go back one dir
            
            else:
                stack.append(item)
        
        return "/" + "/".join(stack)


