# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(r,c, index):
            if index == len(word):
                return True
            
            if r < 0 or c < 0 or r >= rows or c >=cols or board[r][c] != word[index] or (r,c) in visited:
                return False
            
            visited.add((r,c))
            res = dfs(r+1, c, index+1) or dfs(r,c+1, index+1) or dfs(r-1,c, index+1) or dfs(r,c-1, index+1) 
            visited.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False

