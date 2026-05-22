# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style 
# starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

# You start on square 1 of the board. In each move, starting from square curr, do the following:

# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, 
# regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or 
# ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

# Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder 
# is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. 
# You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

 

# Example 1:


# Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation: 
# In the beginning, you start at square 1 (at row 5, column 0).
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 and must take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# This is the lowest possible number of moves to reach the last square, so return 4.


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        #n x n board
        #start bottom left and alternates

        #   12 11 10 9 8 
        #  1 2 3 4 5 6 7 
        #start square 1

        #snake or ladder  if not -1
        #key question, how do we convert a value on board to a cell? r.c , assumewe have this
        #note: shortest -> bfs
        #also if we start at 1, possible dice rolls -> 2,3,4,5,6,7
        # now immagine were at 2, what possible? 3,4,5,6,7, but these are already we saw, so we can keep track of visited

        length = len(board)

        board.reverse() #because were starting at last row thats where 1 is, mkaes more sense to start from top

        #helper method to int to pos

        def inttopos(square):
            #since we start at 1, each element will be + 1 so we subtract -1 to get row we just value / length

            r = (square  - 1) // length
            c = (square - 1) % length #calculates column makes sense, works as long as row is not odd
            if r % 2 != 0: #is odd
                c = length - c - 1
            
            return [r,c]


        #bfs
        q = deque()
        q.append((1,0)) #(squareinInt, how many moves it took us to get to this square)
        visited = set()

        while q :
            square, moves = q.popleft()

            for diceRoll in range(1,7): #dice roll 1-6 moves
                nextSquare = square + diceRoll
                r, c = inttopos(nextSquare)

                #-1 is ladder or snake
                if board[r][c] != -1:
                    nextSquare = board[r][c] 
                
                if nextSquare == length * length:
                    return moves + 1
                
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append((nextSquare, moves + 1))
        return -1

