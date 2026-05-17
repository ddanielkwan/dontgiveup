# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

# While moving from building i to building i+1 (0-indexed),

# If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
# If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

 

# Example 1:


# Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
# Output: 4
# Explanation: Starting at building 0, you can follow these steps:
# - Go to building 1 without using ladders nor bricks since 4 >= 2.
# - Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
# - Go to building 3 without using ladders nor bricks since 7 >= 6.
# - Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
# It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        
        #we dont know when to use bricksor ladders?
        #maybe use to keep track of differentials and if we see larger diff that cant reach maybe we should use ladder

        #greedy
        #look you can keep going and just assume to keep using bricks

        # eventually when your bricks is negative, it means you ont have enoughbricks, so now thatmeans youneeed to check if tehre ladder

        #now obvisouly we want to use ladder for highest bricks,
        #so w pop from our maxHeap
        #and add that back
        heap = [] #max heaps of bricks used 


        for i in range(len(heights)-1): #because we check i+1 to get diff
            diff = heights[i+1] - heights[i]

            if diff <= 0 : #dont need resources
                continue

            #assuem everytime we justuse bricks
            #at some point bricks will be negative
            bricks -= diff

            heapq.heappush(heap, -diff)

            if bricks < 0 : #bricks will benegative if we dont have enough
                if ladders == 0:
                    return i #furthest we can reach is i we ran out
                
                #but if we have ladder lets use it, and add back the bricks
                ladders -= 1
                bricks += -heapq.heappop(heap)
        
        return len(heights)-1 #weve reached end
            

