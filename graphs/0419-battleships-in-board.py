# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', 
# return the number of the battleships on board.

# Battleships can only be placed horizontally or vertically on board. 
# In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column),
#  where k can be of any size. At least one horizontal or vertical cell separates between two battleships 
# (i.e., there are no adjacent battleships).

 

# Example 1:


# Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# Output: 2


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        #m x n board
        # X battleship
        # "." empty

        #find number of bttleships on board
        #isnt this just number of islands?

        #can be simplier 
        # Count only the “starting cell” of each battleship.

        #no ships above, no ships to left

        rows = len(board)
        cols = len(board[0])

        battleships = 0

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    if (r == 0 or board[r-1][c] != 'X') and (c == 0 or board[r][c-1] != 'X'):
                        battleships += 1
        
        return battleships