
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

# Return the number of closed islands.

 

# Example 1:



# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation: 
# Islands in gray are closed because they are completely surrounded by water (group of 1s).


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        #0 land
        #1 water

        #compeltelt surroudned by water

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def dfs(r,c): #detemrine if island is surroudned
            if r < 0 or c < 0 or r>=rows or c >=cols:
                return False #oob not surroudned by water
            
            if grid[r][c] == 1 or (r,c) in visited:
                return True
            visited.add((r,c))
            top = dfs(r+1,c)
            bot = dfs(r-1,c)
            left= dfs(r,c+1)
            right = dfs(r,c-1)  

            return top and bot and left and right #all has to be surrrounded
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r,c) not in visited:
                    if dfs(r,c):
                        islands += 1
        return islands
        

            

