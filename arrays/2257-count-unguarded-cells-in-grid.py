# You are given two integers m and n representing a 0-indexed m x n grid. 
# You are also given two 2D integer arrays guards and walls where
# guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

# A guard can see every cell in the four cardinal directions (north, east, south, or west)
#  starting from their position unless obstructed by a wall or another guard. 
# A cell is guarded if there is at least one guard that can see it.

# Return the number of unoccupied cells that are not guarded.

 

# Example 1:


# Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
# Output: 7
# Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
# There are a total of 7 unguarded cells, so we return 7.

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid = [[0] * n for _ in range(m)]

        #0 is free
        #1 is gurad

        #2 is wall
        #3 is guardable

        for r,c in guards:
            grid[r][c] = 1
        for r,c in walls:
            grid[r][c] = 2
        #simulation
        def mark_guarded(r,c):
            #down
            for row in range(r+1, m): #+1 becase r is already where guard is 
                if grid[row][c] in [1,2]:
                    break
                grid[row][c] = 3
            #up
            for row in reversed(range(0, r)):

                if grid[row][c] in [1,2]:
                    break
                grid[row][c] = 3
            #right
            for col in range(c+1, n):
                if grid[r][col] in [1,2]:
                    break
                grid[r][col] = 3
            #left
            for col in reversed(range(0,c)):
                if grid[r][col] in [1,2]:
                    break
                grid[r][col] = 3

        for r,c in guards:
            mark_guarded(r,c)
        res = 0
        for row in grid:
            for n in row:
                if n == 0:#free
                    res += 1

        return res