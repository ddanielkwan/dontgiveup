# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1).
#  The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. 
# When the ball stops, it could choose the next direction.

# Given the m x n maze, the ball's start position and the destination, 
# where start = [startrow, startcol] and destination = [destinationrow, destinationcol], 
# return true if the ball can stop at the destination, otherwise return false.

# You may assume that the borders of the maze are all walls (see examples).

# Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
# # 


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        #0 empty space
        #walls 1

        #ball in a mze
        #ball can go through empty spaces four directions but wont stop until hits a wall

        #stop can choose next dir

        #start position, and dest

        #bfs

        rows = len(maze)
        cols = len(maze[0])

        visited = [[False]*cols for _ in range(rows)]

        q = deque()
        q.append(start)
        visited[start[0]][start[1]] = True

        dirX = [0, 1, 0, -1]
        dirY = [-1, 0, 1, 0]

        while q:
            currentSpot = q.popleft()
            if currentSpot[0] == destination[0] and currentSpot[1] == destination[1]:
                return True
            
            for i in range(4):
                r = currentSpot[0]
                c = currentSpot[1]
                #potential next r,c if within bound and is empty space
                #keep going until hits wall
                while r >= 0 and r < rows and c >= 0 and c < cols and maze[r][c] == 0:
                    r += dirX[i]
                    c += dirY[i]

                #note we need to remove last cell because hits walleventually
                r -= dirX[i]
                c -= dirY[i]

                if not visited[r][c]:
                    q.append([r,c])
                    visited[r][c] = True
        return False


