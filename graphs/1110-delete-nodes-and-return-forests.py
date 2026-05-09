# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

 

# Example 1:


# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# Example 2:

# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        #root of binary 
        #distinct values

        #so its like chopping it off

        #remaining forests

        #go through dfs
        #have a reference to the parent
        #everytime it reaches the to_delete node 
        #make parent cut off the side that has it 

        #cases
        # delete [1]
        #      1          ->     2    3
        #     / \
        #    2   3


         # delete [2]
        #      1          ->     [1 ->  3], [4]
        #     / \
        #    2   3
        #.  /
        #.  4.

         # delete [4]
        #      1         
        #     / \
        #    2   3
        #.  /
        #.   

        #delete bottom up
        # run dfs on everything, and then if the node is i want to delete
        #then return null to the parent  
        #collecting the roots is top down
        #everytime you go to node, add it to set, if it is to delete, remove it from set

        to_delete = set(to_delete)    
        result_set = set([root])

        def dfs(node):
            if not node:
                return None
            res = node #assume not delete node
            #if we do deelte it
            if node.val in to_delete:
                res = None

                result_set.discard(node) #.discard(node) removes an element from a set without throwing an error if it doesn't exist

                #if the there is left and right we want to add those roots to the result set
                if node.left:
                    result_set.add(node.left)
                if node.right:
                    result_set.add(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return res
        dfs(root)
        return list(result_set)
         




