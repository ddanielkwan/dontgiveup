# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

# You may change 0's to 1's to connect the two islands to form one island.

# Return the smallest number of 0's you must flip to connect the two islands.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 1
# Example 2:

# Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:

# Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #n x n 
        #1 is land 0 water

        ##two isalnds in each grid

        #bfs
        rows = len(grid)
        cols = len(grid[0])

        found = False
        islandCoordinates = set() #alrady seen

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in islandCoordinates or grid[r][c] != 1:
                return
            
            islandCoordinates.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            return
        #we jsut need to find one islands coordinates all (r,c) and then do a bfs on all coords

        for r in range(rows):
            if found:
                break
            for c in range(cols):
                if grid[r][c] == 1 :
                    dfs(r,c)
                    found = True
                    break
        #bfs each level

        q = deque(islandCoordinates)
        shortestPath = float('inf')

        swap = 0
        directions = [[1,0], [-1,0], [0,-1], [0,1]]

        while q :
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row = dr + r 
                    col = dc + c 
                    if row in range(rows) and col in range(cols) and (row,col) not in islandCoordinates:
                        if grid[row][col] == 1:
                            shortestPath = min(shortestPath, swap)
                            #we can even optimize and return swap here since other runs irrelevant since shortest will alwys fidn first

                        q.append((row,col))
                        islandCoordinates.add((row,col))
            swap += 1
        return shortestPath

        

