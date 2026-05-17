# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

# Return the number of alternating groups.

# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

# Example 1:

# Input: colors = [0,1,0,1,0], k = 3

# Output: 3

class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        #0 red
        #1 blue
        #intuition : instead of checking every group from scratch maintain the longest valid alternating segment ending at r
        l = 0

        n = len(colors)

        groups = 0

        for r in range(len(colors) + k - 1):
            #a group can start at any index 0 .. n-1 each group spans k consecutive positions wrapping around if needed, thats why -1

            if colors[r%n] == colors[(r-1)%n]:#if its same as previous
                #restart 
                l = r 
            
            if r - l + 1 > k:
                l += 1
            
            if r - l + 1 == k:
                groups += 1
            
        return groups



