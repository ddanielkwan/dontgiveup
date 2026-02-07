# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
# In this case, 6 units of rain water (blue section) are being trapped.


class Solution:
    def trap(self, height: list[int]) -> int:
        #water above a bar is limited by the shorter wall on its left and right

        l = 0
        r = len(height) - 1

        # track the tallest wall seen so far from each side
        leftMax = height[l]
        rightMax = height[r]

        trappedWater = 0


        while l < r:
            
            # process the smaller side (limiting wall)
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                trappedWater += max(0, min(leftMax, rightMax) - height[l])

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                trappedWater += max(0, min(leftMax, rightMax) - height[r])

        return trappedWater