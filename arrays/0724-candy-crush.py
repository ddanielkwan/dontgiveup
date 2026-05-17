# This question is about implementing a basic elimination algorithm for Candy Crush.

# Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

# The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

# If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
# After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
# After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
# If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
# You need to perform the above rules until the board becomes stable, then return the stable board.

 

# Example 1:


# Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
# Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
            #m x n array board

            #board[i][j] type of candy

            # 0 is empty


            #break it down to three steps
#           1. find() that scans the board for groups of three or more adjacent candies and stores their positions in a set
#  q         2. crush() that sets all positions in the crushed set to 0
#           3. a drop()for each column, moves all non-zero candies down to fill the gaps left by crushed candies 
        #repeat

        rows, cols = len(board), len(board[0])

        def find():
            crushed_set = set()
            # r-1 must exist -> r can't be 0
# r+1 must exist -> r can't be 4
# 
            # Check vertically adjacent candies
            for r in range(1, rows - 1):
                for c in range(cols):
                    if board[r][c] == 0:
                        continue
                    if board[r][c] == board[r - 1][c] == board[r + 1][c]:
                        crushed_set.add((r, c))
                        crushed_set.add((r - 1, c))
                        crushed_set.add((r + 1, c))

            # Check horizontally adjacent candies
            for r in range(rows):
                for c in range(1, cols - 1):
                    if board[r][c] == 0:
                        continue
                    if board[r][c] == board[r][c - 1] == board[r][c + 1]:
                        crushed_set.add((r, c))
                        crushed_set.add((r, c - 1))
                        crushed_set.add((r, c + 1))
            return crushed_set


        def crush(crushed_set):
            for (r, c) in crushed_set:
                board[r][c] = 0

        def drop():
            for c in range(cols):
                lowest_zero = -1

                # Iterate over each column
                for r in range(rows - 1, -1, -1): #start at bottom row to up
                    if board[r][c] == 0:
                        lowest_zero = max(lowest_zero, r)

                    # Swap current non-zero candy with the lowest zero.
                    elif lowest_zero >= 0:
                        board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c]
                        lowest_zero -= 1


        crushed_set = find() #positions that need to be popped
        while crushed_set:
            crush(crushed_set)
            drop()
            crushed_set = find()
        
        return board
    

class Solution2:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
            #m x n array board

            #board[i][j] type of candy

            # 0 is empty


            #break it down to three steps
#           1. find() that scans the board for groups of three or more adjacent candies and stores their positions in a set
#  q         2. crush() that sets all positions in the crushed set to 0
#           3. a drop()for each column, moves all non-zero candies down to fill the gaps left by crushed candies 
        #repeat

        m, n = len(board), len(board[0])

#         def find():
#             crushed_set = set()
#             # r-1 must exist -> r can't be 0
# # r+1 must exist -> r can't be 4
# # 
#             # Check vertically adjacent candies
#             for r in range(1, rows - 1):
#                 for c in range(cols):
#                     if board[r][c] == 0:
#                         continue
#                     if board[r][c] == board[r - 1][c] == board[r + 1][c]:
#                         crushed_set.add((r, c))
#                         crushed_set.add((r - 1, c))
#                         crushed_set.add((r + 1, c))

#             # Check horizontally adjacent candies
#             for r in range(rows):
#                 for c in range(1, cols - 1):
#                     if board[r][c] == 0:
#                         continue
#                     if board[r][c] == board[r][c - 1] == board[r][c + 1]:
#                         crushed_set.add((r, c))
#                         crushed_set.add((r, c - 1))
#                         crushed_set.add((r, c + 1))
#             return crushed_set


        def find_and_crush():
            complete = True

            # Check vertically adjacent candies
            for r in range(1, m - 1):
                for c in range(n):
                    if board[r][c] == 0:
                        continue
                    if abs(board[r][c]) == abs(board[r - 1][c]) == abs(board[r + 1][c]):
                        board[r][c] = -abs(board[r][c])
                        board[r - 1][c] = -abs(board[r - 1][c])
                        board[r + 1][c] = -abs(board[r + 1][c])
                        complete = False

            # Check horizontally adjacent candies
            for r in range(m):
                for c in range(1, n - 1):
                    if board[r][c] == 0:
                        continue
                    if abs(board[r][c]) == abs(board[r][c - 1]) == abs(board[r][c + 1]):
                        board[r][c] = -abs(board[r][c])
                        board[r][c - 1] = -abs(board[r][c - 1])
                        board[r][c + 1] = -abs(board[r][c + 1])
                        complete = False

            # Set the value of each candies to be crushed as 0
            for r in range(m):
                for c in range(n):
                    if board[r][c] < 0:
                        board[r][c] = 0
            return complete

        def crush(crushed_set):
            for (r, c) in crushed_set:
                board[r][c] = 0

        def drop():
            for c in range(n):
                lowest_zero = -1

                # Iterate over each column
                for r in range(m - 1, -1, -1): #start at bottom row to up
                    if board[r][c] == 0:
                        lowest_zero = max(lowest_zero, r)

                    # Swap current non-zero candy with the lowest zero.
                    elif lowest_zero >= 0:
                        board[r][c], board[lowest_zero][c] = board[lowest_zero][c], board[r][c]
                        lowest_zero -= 1



        while not find_and_crush():

            drop()

        
        return board

