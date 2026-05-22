# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


# Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 

# Example 1:

# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]



class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)

        directions = [[1,2],[2,1], [2,-1],[1,-2], [-1,-2], [-2,-1],[-2,1], [-1,2]]

        q = deque()

        q.append((0,0))

        moves = 0
        visited = set() #store visited places
        visited.add((0,0))


        while q :

            for _ in range(len(q)):
                r, c = q.popleft()

                #good case,
                #abs because knight moves are symmetric, so we cut the search space but 3/4
                if abs(r) == abs(x) and abs(c) == abs(y):
                    return moves 
                
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c 

                    if (row,col) not in visited and row >= -1 and col >= -1:
                        q.append((row,col))
                        visited.add((row,col))

            moves += 1

        return 


from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        directions = [
            [1, 2], [2, 1],
            [2, -1], [1, -2],
            [-1, -2], [-2, -1],
            [-2, 1], [-1, 2]
        ]

        q = deque()
        q.append((0, 0, 0))  # row, col, moves

        visited = set()
        visited.add((0, 0))

        while q:
            r, c, moves = q.popleft()

            # reached target
            if (r, c) == (x, y):
                return moves

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, moves + 1))