# You are given a map of a server center, represented as a m * n integer matrix grid,
#  where 1 means that on that cell there is a server and 0 means that it is no server
#  Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server.

 

# Example 1:



# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        #1 is server
        #0 no server
        rows = len(grid)
        cols = len(grid[0])

        rowcount = [0] * rows #row as index, count of every single row, the servers
        colcount = [0] * cols

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rowcount[r] += 1
                    colcount[c] += 1
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (rowcount[r] > 1 or colcount[c] > 1):
                    res += 1
        return res



        #two servers communicate if same row or col

        # brute force
# oh so were using found and only adding 1 because that 1 count isbascially count itself at (r,c)
# class Solution:
#     def countServers(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         res = 0

#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == 0:
#                     continue

#                 found = False
#                 for col in range(n):
#                     if col != c and grid[r][col] == 1:
#                         found = True
#                         break

#                 if not found:
#                     for row in range(m):
#                         if row != r and grid[row][c] == 1:
#                             found = True
#                             break

#                 if found:
#                     res += 1

#         return res

