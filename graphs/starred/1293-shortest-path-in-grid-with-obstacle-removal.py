# you are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

# Example 1:


# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # m x n matrix
        #0 empty 
        #1 obstacles

        #up down left right #one step

        #find min steps to wlak from top left (0,0) to (m-1, n-1)
        #at most you can remove k obstacles

        #-1 if not possible 


        #is this a dp problem or bfs 
        #not dp
     # Because the structure of the problem is fundamentally “Find the shortest path in a graph.”
        # Not:
        # “Build answers from smaller subproblems.”

        #do we store, r,c, steps, kremaining


        visited = set() #we need to store r,c and k becausae (2,3,k=3) is differnet from (2,3,k=0) #you can get more paths
        steps = 0
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        q.append((0,0, k))

        directions = [[-1,0],[1,0], [0,-1], [0,1]]
        while q :
            for _ in range(len(q)):
                r, c, remainingK = q.popleft()

                if (r,c) == (rows-1, cols-1):
                    return steps
                
                for dr, dc in directions:
                    newR, newC = dr + r , dc + c
                    if not (0 <= newR < rows and 0 <= newC < cols):
                        continue
                    
                    newK = remainingK
       
                    if grid[newR][newC] == 1:
                        if newK == 0:
                            continue
                        newK -= 1 #mutating the k
                    if (newR,newC, newK) in visited:
                        continue
                    visited.add((newR,newC,newK))
                    q.append((newR,newC, newK))

            steps += 1 
        return -1



