# You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

# 1 which means a street connecting the left cell and the right cell.
# 2 which means a street connecting the upper cell and the lower cell.
# 3 which means a street connecting the left cell and the lower cell.
# 4 which means a street connecting the right cell and the lower cell.
# 5 which means a street connecting the left cell and the upper cell.
# 6 which means a street connecting the right cell and the upper cell.

# You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

# Notice that you are not allowed to change any street.

# Return true if there is a valid path in the grid or false otherwise.



class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dirs = {
            1: [(0,-1), (0,1)],      # left right
            2: [(-1,0), (1,0)],      # up down
            3: [(0,-1), (1,0)],      # left down
            4: [(0,1), (1,0)],       # right down
            5: [(0,-1), (-1,0)],     # left up
            6: [(0,1), (-1,0)]       # right up
        }


        # From current cell:
                # try all directions this street allows
                # move to neighbor
                # BUT verify neighbor connects back
        # Suppose:
        #     dx, dy = (0,1)   # moving right
        #     Then neighbor must support:
        #     (-dx, -dy) = (0,-1)
        #     That means it connects back
        m, n = len(grid), len(grid[0])

        q = deque() 
        q.append((0,0))
        visited = set([(0,0)])

        while q :
            r, c = q.popleft()

            if (r,c) == (m-1, n-1):
                return True
            
            for dx, dy in dirs[grid[r][c]]:
                nr,nc = dx + r, dy + c
                #not within bounds skip
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                #we already visitedd #skip
                if (nr, nc) in visited:
                    continue
                
                # neighbor must connect back
                if (-dx, -dy) in dirs[grid[nr][nc]]:
                    visited.add((nr, nc))
                    q.append((nr, nc))
        return False