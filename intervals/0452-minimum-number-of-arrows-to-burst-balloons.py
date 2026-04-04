# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

# Example 1:

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
# Example 2:

# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
# Example 3:

# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = len(points) #worse case for now

        previous = points[0] #start,end

         #think about line, if you have [1,6] [2,8]
        #what is the intersection? we set the intersection as previous
        #the intersection is [2,6] so if we have the next [4,8]
        #we check it with the previous to see if it intersects
        #we take the end as the min betewen currentend and previous end

        for i in range(1,len(points)):
            current = points[i]

            if current[0] <= previous[1] : #start less than previosu end
                arrows -= 1 #can use same arrow to pop
                previous = [current[0], min(previous[1], current[1])]
            else:
                previous = current #do nothing
        return arrows