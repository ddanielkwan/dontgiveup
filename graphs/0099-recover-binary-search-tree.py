# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

# Example 1:


# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]
# Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """


        # inorder traversal of BST should be sorted
        # If two nodes are swapped:
        # there will be inversions

        # 1 2 3 4 5
        # Swapped:
        # 1 4 3 2 5
        # Notice:
        # 4 > 3
        # 3 > 2
        self.first = None
        self.second = None
        self.prev = TreeNode(float("-inf"))
        def inorder(node):

            if not node:
                return

            inorder(node.left)

            # violation found
            if self.prev.val > node.val:

                # first violation
                if not self.first:
                    self.first = self.prev

                # always update second
                self.second = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        # swap back
        self.first.val, self.second.val = (
            self.second.val,
            self.first.val
        )

       
