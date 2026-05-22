# Given a NORMAL binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia:
#  “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        #idea Did this subtree contain node p? Did this subtree contain node q?When a node’s subtree contains both, that node is the LCA.
        def dfs(node):
            #we will return hasp, hasq
            nonlocal lca
            if not node:
                #empty
                return [False, False]
            if lca: #no need to contineu further, stop exploring
                return [False, False]

            left = dfs(node.left)
            right = dfs(node.right)

            res = [left[0] or right[0] or (node == p), left[1] or right[1] or (node == q)]
            if res[0] and res[1] and not lca:
                lca = node #The moment a node can say "yes my subtree has p AND yes my subtree has q" — that node is the LCA.
                # The not lca guard makes sure you only set it once, because once found,
                #  every ancestor above will also see both as true, but you don't want to overwrite

            return res 

        dfs(root)
        return lca

