# Given a binary tree root and an integer target, delete all the leaf nodes with value target.

# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

 

# Example 1:



# Input: root = [1,2,3,2,null,2,4], target = 2
# Output: [1,null,3,null,4]
# Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
# After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right,target)

        if not root.left and not root.right and root.val == target:
            return None
        
        return root
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        # if not root:
        #     return None
        
        # root.left = self.removeLeafNodes(root.left, target)
        # root.right = self.removeLeafNodes(root.right,target)

        # if not root.left and not root.right and root.val == target:
        #     return None
        
        # return root

        stack = [root]

        visit = set()

        parents = {root : None}

        while stack:
            node = stack.pop()
            #check leaf node
            if not node.left and not node.right:
                if target == node.val:
                    p = parents[node] 
                    if not p:
                        #no parent, msut be root node
                        return None
                    #left or right child?
                    if p.left == node:
                        p.left = None
                    if p.right == node:
                        p.right = None
            elif node not in visit:
                visit.add(node) #we need visit because of post processing, process child first
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                    parents[node.left] = node
                
                if node.right:
                    stack.append(node.right)
                    parents[node.right] = node
        return root
