# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). 
# An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

# Return the number of islands in grid2 that are considered sub-islands.

 

# Example 1:


# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
# Example 2:


# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2 
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        #1 land
        #0 water

        #grid2 is subset
        rows = len(grid2)
        cols = len(grid2[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid2[r][c]== 0:
                return True
            
            isSubIsland = grid1[r][c] == 1
            #it is subisland true because even if super set is 1 but subset grid2 is 0 still subisland

            grid2[r][c] = 0
            for dr, dc in directions:
                row = dr + r
                col = dc + c

                if not dfs(row,col):
                    isSubIsland = False
            
            return isSubIsland

        numberOfSubIslands = 0

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    if dfs(r,c):
                        numberOfSubIslands += 1
        
        return numberOfSubIslands

