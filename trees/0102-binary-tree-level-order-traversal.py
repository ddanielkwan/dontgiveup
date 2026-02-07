# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #add first level which is root
        q = deque()
        q.append(root)
        res = []

        while q :
            level = []
            for _ in range(len(q)): #we are going to loop through range of current iteration, this means
                #all nodes at this level, and we just add its children but dont process until next level
                node = q.popleft()

                if node:
                    q.append(node.left)
                    q.append(node.right)

                    level.append(node.val)
            if level:
                res.append(level)
        
        return res

