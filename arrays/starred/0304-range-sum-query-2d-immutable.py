# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity



class NumMatrix:
    
    def __init__(self, matrix: list[list[int]]):
        #we can calculate using prefix sum, imagine the bottom right of the square will store the sum from top cell prefix and left prefix
        #we have to add extra row on top and extra row on left because edge case if its square on top left, we have to substract the squares above and left oob
        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.sumMatrix = [[0] * (COLS + 1) for r in range(ROWS + 1 )] 
        #the matrix is not same size as sumMatrix, need offset by 1
        for r in range(ROWS):
            prefix = 0 #for any row we want prefix sum of that row
            for c in range(COLS):
                prefix += matrix[r][c] #this is to the left 
                above = self.sumMatrix[r + 1 - 1][c + 1] #the row above, and same column
                self.sumMatrix[r+1][c+1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #use theseon summatrix
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        totalArea = self.sumMatrix[row2][col2]
        aboveArea = self.sumMatrix[row1-1][col2]
        leftArea = self.sumMatrix[row2][col1 - 1]
        topLeftArea = self.sumMatrix[row1 - 1][col1 - 1]

        return totalArea - aboveArea - leftArea + topLeftArea
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

