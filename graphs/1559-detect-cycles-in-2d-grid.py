# Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

# A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

# Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

# Return true if any cycle of the same value exists in grid, otherwise, return false.

 

# Example 1:



# Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
# Output: true



class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(r, c, pr, pc):  # fixed: track parent position
            if (r, c) in visited:
                return True     #revisiting = cycle
            
            visited.add((r, c))
            directions = [[1,0], [-1,0],[0,1], [0,-1]]
        # so the reason we didnt add check for length 4 is becase its imposisble to cycle in grid if less than 4
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if row < 0 or col < 0 or row >= rows or col >= cols:
                    continue
                if (row, col) == (pr, pc):
                    continue    #  skip wnere it came from parent position not value
                if grid[row][col] != grid[r][c]:
                    continue    # skip different characters
                if dfs(row, col, r, c):
                    return True

            return False     
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:           #skip already visited
                    if dfs(r, c, -1, -1):
                        return True
        
        return False