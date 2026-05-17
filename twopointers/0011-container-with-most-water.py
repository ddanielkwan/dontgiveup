# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) 
# and (i, height[i]).

# Find two lines that together with the x-axis form a container,
#  such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        #intuition: if the length on either left or ride side is higher, why would we move that pointer?
        #we want to keep the higher side, the limit of area is limited by which side is shortest, we want to find highest side
        #calculate area for each time and keep changing whichever side smaller
        l = 0
        r = len(height) - 1
        
        maxArea = 0

        while l < r :

            currentArea = (r - l ) * min(height[l], height[r])
            maxArea = max(currentArea, maxArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea

