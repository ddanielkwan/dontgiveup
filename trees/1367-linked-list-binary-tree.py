# Given a binary tree root and a linked list with head as the first node. 

# Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

# In this context downward path means a path that starts at some node and goes downwards.

 

# Example 1:



# Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Explanation: Nodes in blue form a subpath in the binary Tree. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def helper(listNode, treeNode):
            if not listNode:
                return True #weve reached end of list
            
            if not treeNode or listNode.val != treeNode.val:
                return False

            return (helper(listNode.next, treeNode.left) or helper(listNode.next, treeNode.right))
        
        if helper(head, root):
            return True
        #if head not match root
        #we want to compare root.left with ehad and root.right with head
        if not root:
            return False
        return self.isSubPath(head,root.left) or self.isSubPath(head, root.right)

