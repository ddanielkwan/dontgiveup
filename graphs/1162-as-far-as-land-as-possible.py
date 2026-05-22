# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land,
#  find a water cell such that its distance to the nearest land cell is maximized, and return the distance.
#  If no land or water exists in the grid, return -1.

# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

# Example 1:


# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        #0 water
        #1 land
        #find watercell such taht distance to nearest land is maximized
        #bfs

        q = deque()

        visited = set()
        rows = cols = len(grid)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r,c,0))
                    visited.add((r,c))
        
        distance = float('-inf')
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q :
            for _ in range(len(q)):
                r,c , d = q.popleft()
                #we dont need to sue manhanntan to calcualte formula dsitane because bfs is laready calcualting
                
                distance = max(distance,d)
                for dr, dc in directions:
                    row = dr + r 
                    col = dc + c 

                    if row in range(rows) and col in range(cols) and (row,col) not in visited:
                        if grid[row][col] == 0:
                            grid[row][col] = distance
                            visited.add((row,col))
                            q.append((row,col, distance +1))
        if distance != float('-inf') and distance != 0:
            return distance
        return -1

