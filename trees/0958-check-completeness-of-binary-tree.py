# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled,
#  and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        #bfs
        #look at every level
        #if we see a null means we started to end
        #so if we see another val after that end means its false

        q = deque()

        q.append(root)
        end = False

        while q :
            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    if end:
                        return False
                    q.append(node.left)
                    q.append(node.right)
                else:
                    end = True
        return True

