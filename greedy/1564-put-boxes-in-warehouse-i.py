# You are given two arrays of positive integers, boxes and warehouse, representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. The warehouse's rooms are labelled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

# Boxes are put into the warehouse by the following rules:

# Boxes cannot be stacked.
# You can rearrange the insertion order of the boxes.
# Boxes can only be pushed into the warehouse from left to right only.
# If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped before that room.
# Return the maximum number of boxes you can put into the warehouse.

 

# Example 1:


# Input: boxes = [4,3,4,1], warehouse = [5,3,3,4,1]
# Output: 3
# Explanation: 

# We can first put the box of height 1 in room 4. Then we can put the box of height 3 in either of the 3 rooms 1, 2, or 3. Lastly, we can put one box of height 4 in room 0.
# There is no way we can fit all 4 boxes in the warehouse.

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # boxes = [4,3,4,1] it doesnt ahve to go into this order, we choose the order 
        # The warehouse has a physical constraint — to reach room i, a box must pass through all previous rooms. So the effective height of room i is limited by the smallest room before it
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i-1])

        boxes.sort()
        warehouse.sort()

        print(boxes)
        print(warehouse)
        b = 0
        w = 0
        res = 0

        while b < len(boxes) and w < len(warehouse):
            if boxes[b] <= warehouse[w]:
                res += 1
                b += 1
            w += 1
        
        
        return res
            

