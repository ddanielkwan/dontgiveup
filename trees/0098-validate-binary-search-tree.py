# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #use an interval to be passed down
        def dfs(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            left = dfs(node.left, left, node.val)
            right = dfs(node.right, node.val, right)
            
            return left and right
        return dfs(root, float('-inf'), float('inf'))

