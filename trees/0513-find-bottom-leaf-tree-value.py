# Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

# Example 1:


# Input: root = [2,1,3]
# Output: 1
# Example 2:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxDepth, self.res = -1, root.val
        #dont get fooled, you can have all right side tree
        
        def dfs(node, depth):
            if not node:
                return
            if depth > self.maxDepth:
                self.maxDepth, self.res = depth, node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return self.res
    
    #   q = deque([root])

    #     while q:
    #         node = q.popleft()
    #         if node.right:
    #             q.append(node.right)
    #         if node.left:
    #             q.append(node.left)

    #     return node.val

