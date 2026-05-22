

# Given the root of a binary tree, imagine yourself standing on the right side of it,
#  return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:

# Input: root = [1,2,3,null,5,null,4]

# Output: [1,3,4]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,null,null,null,5]

# # Output: [1,3,4,5]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # q = deque()
        # q.append(root)

        # res = []

        # while q :
        #     last = None
        #     for _ in range(len(q)):
        #         node = q.popleft()

        #         if node:
        #             last = node
        #             q.append(node.left)
        #             q.append(node.right)
        #     if last:
        #         res.append(last.val)
        
        # return res

        res = []

        prev = -1 
        def dfs(node, depth):
            nonlocal prev
            if not node:
                return

            if prev < depth :
                prev = depth 
                res.append(node.val)
            
            dfs(node.right, depth + 1 )
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res

