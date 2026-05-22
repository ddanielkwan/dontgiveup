# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
#  A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = root.val

        def dfs(root):
            #were going to have 2 things
            #1. our return will be best single path(with no split) going upwards
            #2. there will be caclulaiotn each iteration for leftmax + rightmax + root.val
            nonlocal res
            if not root:
                return 0
           
            # get the best path sum from left and right subtrees
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0) #can be < 0 just discard because adding makes worse
            rightMax = max(rightMax, 0)

            #idea: it makes sense that the max path sum should be adding both current node and the max from left side and right side

        
            res = max(res, root.val + leftMax + rightMax)

            # case 2: return the best SINGLE path going upward to parent
            # parent can only choose ONE side, not both
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res

