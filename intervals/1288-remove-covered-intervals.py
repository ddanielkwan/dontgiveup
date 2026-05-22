# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), 
# remove all intervals that are covered by another interval in the list.

# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

# Return the number of remaining intervals.

 

# Example 1:

# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
# Example 2:

# Input: intervals = [[1,4],[2,3]]
# Output: 1


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #[[1,4], [2,8], [3,6]]

        intervals.sort(key = lambda x : (x[0], -x[1]))
        #-x[1] means we want the largest end first , and smallest begibnning
        #[1,5],[1,3],[1,2]

        remaining_intervals = len(intervals)

        prevStart, prevEnd = intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            #if the followed interval is within our current bounds inner, then we must add that to overall total
            if prevStart <= start and prevEnd >= end:
                remaining_intervals -= 1
            
             #what if partially covered?
            #[1,4] , [2,6] > we treat that becomes as [1,6]
            elif start <= prevEnd:
                prevStart = min(start, prevStart)
                prevEnd = max(end,prevEnd)
            else:
                #good no overlap
                prevStart, prevEnd = start, end
        return remaining_intervals

