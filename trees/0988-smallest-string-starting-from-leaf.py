# You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

# Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

# As a reminder, any shorter prefix of a string is lexicographically smaller.

# For example, "ab" is lexicographically smaller than "aba".
# A leaf of a node is a node that has no children.

 

# Example 1:


# Input: root = [0,1,2,3,4,3,4]
# Output: "dba"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return ""

        smallest = None #global vairalbe
        q = deque() #sttore node, current string
        #we use chr(ord('a') + node.val) to convert the node’s number (0–25) into its corresponding lowercase letter ('a' to 'z')

        q.append((root, chr(root.val + ord('a'))))

        while q :
            node, string = q.popleft()

            if not node.left and not node.right: #we have to make sure it is the last node
                if not smallest or string < smallest:
                    smallest = string
            
            if node.left:
                q.append([node.left, chr(ord('a')+node.left.val) + string]) #add in front
            if node.right:
                q.append([node.right, chr(ord('a')+node.right.val) + string]) 
        return smallest

