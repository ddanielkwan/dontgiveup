# You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points 
# at position (r, c) on the matrix. 
# Two robots are playing a game on this matrix.

# Both robots initially start at (0, 0) and want to reach (1, n-1). 
# Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).

# At the start of the game, the first robot moves from (0, 0) to (1, n-1), 
# collecting all the points from the cells on its path. For all cells (r, c) traversed on the path, 
# grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), 
# collecting the points on its path. Note that their paths may intersect with one another.

# The first robot wants to minimize the number of points collected by the second robot. 
# In contrast, the second robot wants to maximize the number of points it collects. 
# If both robots play optimally, return the number of points collected by the second robot.

class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        #to minimize number of points collected by second robot, means to maximize number of points first robot collects
        #we can use prefix sum for each row, because if you imagine the grid, once the first robot crosses down
        #the second robot can only either collect the points on top after that intersection, or on bottom before that intersection

        columns = len(grid[0])
        topRowPrefix = grid[0].copy()
        bottomRowPrefix = grid[1].copy()

        #calculate the prefix for both top and bottom, we will use this later to determine the calculation of what is left
        #by using (index) in the for loop

        #skip col 1 since prefix already calculated
        for idx in range(1, columns):
            topRowPrefix[idx] += topRowPrefix[idx - 1]
            bottomRowPrefix[idx] += bottomRowPrefix[idx - 1]
        
        secondRobotPoints = float("infinity")

        for possibleFirstRobotDirectionChange in range(columns):
            topRowRemaining = topRowPrefix[-1] -  topRowPrefix[possibleFirstRobotDirectionChange]
            bottomRowRemaining = bottomRowPrefix[possibleFirstRobotDirectionChange - 1] if possibleFirstRobotDirectionChange > 0 else 0
            secondRobot = max(topRowRemaining, bottomRowRemaining)
            
            secondRobotPoints = min(secondRobotPoints, secondRobot)
        return secondRobotPoints


        

