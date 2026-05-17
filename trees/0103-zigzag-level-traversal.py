# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque()
        q.append(root)

        leftToRight = True
        res = []

        while q :
            size = len(q)
            level = [0] * size
            for i in range(size):
                node = q.popleft()

                index = i if leftToRight else size - i - 1
                #determien index to insert, and then insert at res level

                level[index] = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            leftToRight = not leftToRight
            #flip tor zigzaggy

            if level:
                res.append(level)

        return res

