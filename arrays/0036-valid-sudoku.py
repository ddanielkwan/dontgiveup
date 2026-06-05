# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules



from collections import defaultdict

#USE HASHMAP TO STORE VALUES OF EACH ROW COL AND SQUARE
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        
        for r in range(9):
            #each row
            row = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row:
                    return False
                row.add(board[r][c])
        
        for c in range(9):
            col = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in col:
                    return False
                col.add(board[r][c])

        #the key is  (r//3, c//3)
# Rows/Cols   0 1 2   3 4 5   6 7 8
#               +-------+-------+-------+
# 0 1 2         |  0 0 0|  1 1 1|  2 2 2|
#               |  0 0 0|  1 1 1|  2 2 2|
#               |  0 0 0|  1 1 1|  2 2 2|
#               +-------+-------+-------+
# 3 4 5         |  3 3 3|  4 4 4|  5 5 5|
#               |  3 3 3|  4 4 4|  5 5 5|
#               |  3 3 3|  4 4 4|  5 5 5|
#               +-------+-------+-------+
# 6 7 8         |  6 6 6|  7 7 7|  8 8 8|
#               |  6 6 6|  7 7 7|  8 8 8|
#               |  6 6 6|  7 7 7|  8 8 8|
#               +-------+-------+--------
        seen = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                key = (r//3, c//3)
                if  board[r][c] in seen[key]:
                    return False
                seen[key].add(board[r][c])

        return True



