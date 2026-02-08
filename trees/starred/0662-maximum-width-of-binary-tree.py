# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

# It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

# Example 1:


# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #idea: we need to use bfs, we need to get the last level's distance between first node and last node
        #normally we would store 2 elements, this time
        #we store 3 elements, [node, number, level we are on]
        #another note, we do not care about what value the node has
        #we take advantage of at any node, its children left and right is root * 2 + 1
        #e.g root(1) x 2 = 2 = left and root(1) x 2 + 1 = 3 right

        #were going to use the variable level to check when we switch to a different level
        #the moment we switched to a different level, we set that as the first value to use to subtract, since thats the very first number
        #and we continue to calculate res by doing every other node - prevnum

        q = deque()
        res = 0 
        q.append([root,1, 0])

        prevLevel = 0
        firstNum = 1 #this is the first node on the row and we use the last num to subtracrt this

        while q :
            node, currentNumber, level = q.popleft()
            #if level is different we set the first val as this
            if level > prevLevel:
                prevLevel = level
                firstNum = currentNumber
            res = max(res, currentNumber - firstNum + 1 )

            if node.left:
                q.append([node.left, currentNumber * 2 , level + 1])
            if node.right:
                q.append([node.right, currentNumber * 2 + 1 , level + 1])
        return res