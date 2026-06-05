# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
# (i.e., from left to right, level by level from leaf to root).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        result = []
        #bfs then reverse it 

        if not root:
            return result

        q = deque([root])

        while q :
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:    

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    level.append(node.val)
            if level:
                result.append(level)
        return result[::-1]
