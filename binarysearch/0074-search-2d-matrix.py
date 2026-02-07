# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 



class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        l = 0

        r = len(matrix) - 1

        #binary search to find target
        #step 1 : find the array which the target could lie in

        while l <= r :

            m = l + (r-l)//2
            row = matrix[m]

            if row[0] > target:
                r = m - 1
            elif row[-1] < target:
                l = m + 1
            else: 
                break
        
        #step 3 binary search on the array we found
        l = 0
        r = len(row) - 1

        while l <= r :

            m = l + (r-l)//2

            if row[m] < target:
                l = m + 1
            elif row[m] > target:
                r = m - 1
            else:
                return True
        
        return False
            



