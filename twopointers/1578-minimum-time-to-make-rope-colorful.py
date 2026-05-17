# Alice has n balloons arranged on a rope. 
# You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

# Alice wants the rope to be colorful. 
# She does not want two consecutive balloons to be of the same color, 
# so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. 
# You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs 
# to remove the ith balloon from the rope.

# Return the minimum time Bob needs to make the rope colorful.

# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        #if multiple adjacent balloons have the same color, we must remove all but one — and we should keep the one that’s most expensive to remove
        #Because removing cheaper ones costs less time
        #return the minimum time Bob needs to make the rope colorful
        timePointer = 0
        time = 0

        for r in range(1,len(colors)): #we start at 1 index, so we can compare with previous
        #if the two balloons are same color, we want to compare pointer we are at now vs pointer we're at before, which neededTime is most, if current pointer is more expensive, then we remove the element at which previous pointer was at, because its cheaper, so we add that to the time
        #we now update that pointer to current pointer, because we removed previous
        #else case, current pointer is faster, so we remove current
        #at any moment, we are only keeping track of two of the same items
        #if not same, just update index pointer to current pointer
            if colors[r] == colors[r-1]:
                if neededTime[r] > neededTime[timePointer]:
                    time += neededTime[timePointer]
                    timePointer = r
                else:
                    time += neededTime[r]
            
            else:
                timePointer = r 
        
        return time


