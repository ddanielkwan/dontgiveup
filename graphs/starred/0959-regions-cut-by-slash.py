# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

# Given the grid grid represented as a string array, return the number of regions.

# Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

# Example 1:


# Input: grid = [" /","/ "]
# Output: 2

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        #make everying a 3x3 grid, we ncat use 2x2

        rows1 = len(grid)
        cols1 = len(grid[0])

        rows2 = 3 *rows1
        cols2 = 3 * cols1

        grid2 = [[0] * cols2 for _ in range(rows2)]


        for r in range(rows1):
            for c in range(cols1):
                r2, c2 = r * 3 , c * 3 
                if grid[r][c] == "/":
                    grid2[r2][c2+2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2] = 1
                elif grid[r][c] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2+2] = 1

        def dfs(r,c, visited):
            if r < 0 or c <0 or r>=rows2 or c >= cols2 or grid2[r][c] == 1 or (r,c) in visited:
                return
            visited.add((r,c))
            directions =[[r+1,c], [r-1,c], [r,c+1], [r,c-1]]
            for r, c in directions:
                dfs(r,c, visited)

        #count numerof regions
        visited = set()
        res = 0
        for r in range(rows2):
            for c in range(cols2):
                if grid2[r][c] == 0 and (r,c) not in visited:
                    dfs(r,c, visited)
                    res += 1
        
        return res




