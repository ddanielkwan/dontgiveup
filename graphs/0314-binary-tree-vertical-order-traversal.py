# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #intuition
        #from the picture seems that if you go right its different column

        #but if that node on right has node left, then it coems bakc to same oclumn
        #maybe we can keep track of col we are on and +1 if go right -1 if go left
        #have hashmap or something

        #we can do a dfs, nevermind ewe cnnot do dfs
        #because it messes up the order
        #think of tree that has left but a lot of extended right
        #we end up adding those rights first to that column before the ones above it


        if not root:
            return []

        columns = defaultdict(list)

        q = deque([(root, 0)])

        while q:

            node, col = q.popleft()

            columns[col].append(node.val)

            if node.left:
                q.append((node.left, col - 1))

            if node.right:
                q.append((node.right, col + 1))

        result = []

        for col in sorted(columns.keys()):
            result.append(columns[col])

        return result