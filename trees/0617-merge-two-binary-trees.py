# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

 

# Example 1:


# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #some way to take two nodes and add them together

        def dfs(first, second):
            if not first and not second:
                return None
            
            firstVal = first.val if first else 0
            secondVal = second.val if second else 0

            node = TreeNode(firstVal + secondVal)

            node.left = dfs(first.left if first else None, second.left if second else None)
            node.right = dfs(first.right if first else None, second.right if second else None)

            return node
        
        return dfs(root1,root2)