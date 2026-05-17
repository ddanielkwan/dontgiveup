# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

# Example 1:


# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.



class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #heights[r][c] height above sea level
        #find all cells that can flow to both pacific and atlantic
        #can only move when adjacent cells is greater

        pacific = set()
        atlantic = set()
        
        rows = len(heights)
        cols = len(heights[0])
        #algo: we only need to check the edges that touhc the oceans
        #so if we go from edge to middle, then we must only go if the next cell is greater than prev
        def dfs(r,c, tracker, prevHeight):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in tracker or prevHeight > heights[r][c]:
                return
            
            tracker.add((r,c))
            dfs(r+1,c, tracker, heights[r][c])
            dfs(r-1,c, tracker, heights[r][c])
            dfs(r,c+1, tracker, heights[r][c])
            dfs(r, c-1, tracker, heights[r][c])
        
        for r in range(rows): 
            dfs(r,0, pacific, heights[r][0]) #first column pacific
            dfs(r, cols-1, atlantic, heights[r][cols-1]) #atlantic
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c , atlantic, heights[rows-1][c])
        
        intersect = []
        for p in pacific:
            if p in atlantic:
                intersect.append(p)
        
        return intersect
            

