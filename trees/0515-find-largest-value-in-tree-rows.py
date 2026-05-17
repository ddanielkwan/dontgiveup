# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

# Example 1:


# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        q = deque()
        q.append(root)

        res = []
        while q:
            maxNumber = float("-inf")
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    maxNumber = max(maxNumber, node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(maxNumber)
        
        return res

