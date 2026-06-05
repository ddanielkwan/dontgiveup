# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

# Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

 

# Example 1:

# Input: intervals = [[1,2]]
# Output: [-1]
# Explanation: There is only one interval in the collection, so it outputs -1.
# Example 2:

# Input: intervals = [[3,4],[2,3],[1,2]]
# Output: [-1,0,1]
# Explanation: There is no right interval for [3,4].
# The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
# The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        for i, interval in enumerate(intervals):
            interval.append(i)

        intervals.sort() #(start,end original index)

        #find first value >= target so its binary search

        
        result = [-1] * len(intervals)
        for _, end, index in intervals:
            res = -1
            l = 0
            r = len(intervals) - 1
            while l <= r :

                m = l + (r-l)//2
                compareStart, _, newIndex = intervals[m]

                if compareStart >= end:
                    #we found potential
                    res = newIndex
                    r = m - 1
                else:
                    l = m + 1

            result[index] = res
        return result


