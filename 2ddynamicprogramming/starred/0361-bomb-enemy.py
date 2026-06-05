# Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.

# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.

 

# Example 1:


# Input: grid


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        #m x n grid
        #W wall
        #E enemy
        #0 empty


        res = 0

        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        rowKills = 0
        colKills = [0] * cols

        for r in range(rows):
            for c in range(cols):
                #calculate row
                #we only need to recalulate row if 
                #1. we are first col
                #2. the previous was a wall
                if c == 0 or c > 0 and grid[r][c-1] == 'W':
                    rowKills = 0

                    i = c
                    while i < cols and grid[r][i] != 'W':
                        if grid[r][i] == 'E':
                            rowKills += 1
                        i += 1
                #calculate col
                #we only calculate col if first row
                # 2. previous row was wall

                if r == 0 or r > 0 and grid[r-1][c] == 'W':
                    colKills[c] = 0
                    i = r
                    while i < rows and grid[i][c] != 'W':
                        if grid[i][c] == 'E':
                            colKills[c] += 1

                        i += 1
                if grid[r][c] == '0':
                    res = max(res, colKills[c] + rowKills)
        return res