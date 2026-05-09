# Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

 

# Example 1:


# Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
# Output: [[7,0,0],[-7,0,3]]
# Example 2:

# Input: mat1 = [[0]], mat2 = [[0]]
# Output: [[0]]

# Time: O(m × k × n)

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(k):
                if mat1[i][j] == 0:  # skip zeros
                    continue
                for l in range(n):
                    result[i][l] += mat1[i][j] * mat2[j][l]
        
        return result