# ou are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

 

# Example 1:


# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        #strange



        #algorithm
        #look at each row and column
        #for each row, and each col look above it and precompute(count how many above)
        #sort the row
        #compute the area

        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
    
        prev_heights = [0] * cols

        for r in range(rows):
            heights = matrix[r][:]
            for c in range(cols):
                if heights[c] > 0 :
                    heights[c] += prev_heights[c]
            sorted_heights = sorted(heights,reverse=True)
            for i in range(cols):
                res = max(res, (i+1) * sorted_heights[i])
            
            prev_heights = heights
        
        return res
#o(m * nlogn)