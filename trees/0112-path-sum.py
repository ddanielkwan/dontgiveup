# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def dfs(node, currentSum):
            if not node: #we've hit the end we cant add anymore
                return False
            
            currentSum += node.val
            if not node.left and not node.right and currentSum == targetSum:
                return True
            
            left = dfs(node.left, currentSum)
            right = dfs(node.right, currentSum)
            return left or right
            

        return dfs(root, 0)