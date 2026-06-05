#You are given two arrays of positive integers, boxes and warehouse, 
# representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. 
# The warehouse's rooms are labeled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

# Boxes are put into the warehouse by the following rules:

# Boxes cannot be stacked.
# You can rearrange the insertion order of the boxes.
# Boxes can be pushed into the warehouse from either side (left or right)
# If the height of some room in the warehouse is less than the height of a box, 
# then that box and all other boxes behind it will be stopped before that room.
# Return the maximum number of boxes you can put into the warehouse.

 

# Example 1:


# Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
# Output: 4
# Explanation:

# We can store the boxes in the following order:
# 1- Put the yellow box in room 2 from either the left or right side.
# 2- Put the orange box in room 3 from the right side.
# 3- Put the green box in room 1 from the left side.
# 4- Put the red box in room 0 from the left side.
# Notice that there are other valid ways to put 4 boxes such as swapping the red and green boxes or the red and orange boxes.


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # o maximize the number of boxes you can place in the warehouse, you should start by placing the smallest box

        #lef and right
        #compute prefix for left and right
        #from left, the max size box you can put is the smallest room height weve seen so far
        #e.g [3,1,2,3] -> [3,1,1,1]
        #same for right
        # -> [1,1,2,3]
        n = len(warehouse)

        # reachable from left
        left = [0] * n
        left[0] = warehouse[0]

        for i in range(1, n):
            left[i] = min(left[i - 1], warehouse[i])

        # reachable from right
        right = [0] * n
        right[-1] = warehouse[-1]

        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], warehouse[i])

        # best possible reachable height
        reachable = [
            max(left[i], right[i])
            for i in range(n)
        ]
        #total for all rooms
        #we sort both and do a greedy
        boxes.sort()
        reachable.sort()

        #two pointers
        i = j = 0
        res = 0

        #boxes [1,1,2,2,3]
        #warehouse [1,1,3,3,3,4]
        #smallest boxes go first 
        while i < len(boxes) and j < n:

            if boxes[i] <= reachable[j]:
                res += 1
                i += 1
                j += 1
            else: #keep increasing if cannot 
                j += 1

        return res