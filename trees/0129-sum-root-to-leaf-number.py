# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0

        # q = deque()
        # q.append([root, root.val])
        
        # res = 0
        # while q :

        #     node, pathsum = q.popleft()

        #     if not node.left and not node.right:
        #         res += pathsum
        #         continue
            
        #     if node.left:
        #         q.append([node.left, pathsum * 10 + node.left.val])
        #     if node.right:
        #         q.append([node.right, pathsum * 10 + node.right.val])
        # return res
        
        res = 0
        def dfs(node, pathSum):
            nonlocal res
            if not node:
                return 0
            pathSum = pathSum * 10 + node.val
            if not node.left and not node.right:
                res += pathSum
                return
            
            dfs(node.left, pathSum)
            dfs(node.right, pathSum)
        dfs(root,0)
        return res

