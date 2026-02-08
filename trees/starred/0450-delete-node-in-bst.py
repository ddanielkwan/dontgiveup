# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val :
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left : #if we delete 3, and pretend 3.right = none, we want to just return node.left(2) and if 3.left = None, we want to return node.right(4), since both of these cases they are both less than parent 5 
            # and case if no left and no right, then return none
        #      5
        #     / \
        #    3
        #   / \
        # 2    4
                return root.right
            elif not root.right:
                return root.left
#             We cannot just delete 3 because then
        # Where do 2 and 4 go?
        # We must keep BST order.
        # So instead, we REPLACE 3 with another value that keeps BST valid
            #find the min from the right subtree, why use the right subtree because if we replace 3, we must choose a value that is bigger than everything on the left so we use minnimum of right side 
            curr = root.right
            while curr.left:
                curr = curr.left #because we need actual node not none
            root.val = curr.val #copy the minimum value into the node we are deleting 
            #nows tehre duplicate, so we go into right side and delete that value
            root.right = self.deleteNode(root.right, root.val)
        return root

        