# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as 
# descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return
        def dfs(node, p, q ):

            if not node:
                return
            #they split 
            if p.val < node.val < q.val or q.val < node.val < p.val:
                return node
            #one of them is higher than other, we have toreturn
            if node.val == p.val :

                return node
            if node.val == q.val:

                return node
            #go right both of them are larger
            if node.val < p.val and node.val < q.val:
                return dfs(node.right, p, q)        
            #go left
            if node.val > p.val and node.val > q.val:
                return dfs(node.left, p, q)
        return dfs(root,p , q)
        

