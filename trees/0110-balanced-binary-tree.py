# Given a binary tree, determine if it is height-balanced.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        


        def dfs(node):

            if not node:
                return [0, True]
            
            left = dfs(node.left)
            right = dfs(node.right)

            balanced = left[1] and right[1] and abs(left[0]- right[0]) <= 1

            return [max(right[0],left[0])+ 1, balanced]
        
        return dfs(root)[1]



