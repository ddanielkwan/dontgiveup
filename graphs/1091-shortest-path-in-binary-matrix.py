# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # n n 
        #length of shortest path

        #what is aclear path
        #top left to bottom right so that alll cells in path is 0
        #and all adj cells of path are 8 diretionall connected;;
        #bfs

        n = len(grid)

        visited = set()
        q = deque([(0,0,1)])

        directions = [[0,1],[0,-1], [1,0],[-1,0], [1,1], [-1,-1],[-1,1],[1,-1]]
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        while q :
            r, c , length = q.popleft()
            if r == n-1 and c == n-1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and
                    (nr, nc) not in visited):
                    q.append((nr, nc, length + 1))
                    visited.add((nr, nc))
        return -1