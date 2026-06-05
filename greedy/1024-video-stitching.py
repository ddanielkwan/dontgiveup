# You are given a series of video clips from a sporting event that lasted time seconds. 
# These video clips can be overlapping with each other and have varying lengths.

# Each video clip is described by an array clips where clips[i] = [starti, endi] 
# indicates that the ith clip started at starti and ended at endi.

# We can cut these clips into segments freely.

# For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
# Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time].
#  If the task is impossible, return -1.

 

# Example 1:

# Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
# Output: 3
# Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
# Then, we can reconstruct the sporting event as follows:
# We cut [1,9] into segments [1,2] + [2,8] + [8,9].
# Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        #intervals 
        #oveflapping
        #clips[i] = start ,end

        #sporting even lasts time long

        #we can cut our clps
        #
        clips.sort()
        #greedy approach
        #greedy approach, we start at current end = 0, we look for all intervals with start <= current_end, and we pick the interval that has largest new end
        #for example : we have two choices for first 0 [[0,2],[0,4], [1,5]]
        #0,2 and 0,4 which one should we pick for next interval? obv the longer end
        #so now our nextend is 4
        #now we check again for all intervals <= 4 and see which inteval goes longest
        #ob we want pick [1,5]
        #if nextend == currn_end means were stuck so -1

        currentMaxEnd = 0
        index = 0 
        clipsNeeded = 0

        nextPossibleEnd = 0



        while currentMaxEnd < time: #in bounds
            #if clips[index][0] <= currentmxaend then get the max
            # so imagine [0,2]
            #then we see 1,9 and 1,5, we choose the larger one, 1,9
            #next possible end is 9
            while index < len(clips) and clips[index][0] <= currentMaxEnd:
                nextPossibleEnd = max(nextPossibleEnd, clips[index][1])
                index += 1

            if currentMaxEnd == nextPossibleEnd :
                return -1
                #not possible
            
            currentMaxEnd = nextPossibleEnd
            clipsNeeded += 1
        return clipsNeeded
            


