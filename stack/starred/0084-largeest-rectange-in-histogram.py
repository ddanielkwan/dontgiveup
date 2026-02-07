# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        #a bar’s maximum width is known only when we find a smaller bar
        #stack keeps bars in increasing height order each bar is waiting to see how far it can extend to the right

        stack = [] #what will we store? (index, val) 
        #note: this index will be the starting index in which this value can start 
        #we willl need to update this start index

        maxArea = 0

        for index, height, in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                i, val = stack.pop()
                maxArea = max(maxArea, val * (index-i))
                start = i
                # we meed to change the start index of tat value

                #example
                #if we have a stack [3,4,5]
                #now if our next element is [1],
                #looking at it, we know 1 can start at index 0
                #so the area for [1] can be 1 + 1+ 1+ 1
                #so we chnget the start for that val
            
            stack.append((start, height))
        
        for index, value in stack:
            #if all monoincreasing start calculating

            maxArea = max(maxArea, value * (len(heights) - index))
        
        return maxArea
            


