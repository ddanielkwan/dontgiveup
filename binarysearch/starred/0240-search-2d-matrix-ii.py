# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
 

# Example 1:


# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #you cannot use double binary search like q 1 because not each row is fgraeter han preivous
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False


        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0
# points to a (row,col) that lies outside of the dimensions of the
# matrix), we do the following: if the currently-pointed-to value is larger
# than target we can move one row "up". Otherwise, if the
# currently-pointed-to value is smaller than target, we can move one column
# "right". It is not too tricky to see why doing this will never prune the
# correct answer; because the rows are sorted from left-to-right, we know that
# every value to the right of the current value is larger. Therefore, if the
# current value is already larger than target, we know that every value to
# its right will also be too large. A very similar argument can be made for the
# columns, so this manner of search will always find target in the matrix (if
# it is present)
        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
        
        return False
    
    #O(n+m)

