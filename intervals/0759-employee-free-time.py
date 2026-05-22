# We are given a list schedule of employees, which represents the working time for each employee.

# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

# Example 1:

# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation: There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # If some interval overlaps any interval (for any employee), then it won't be included in the answer. So we could reduce our problem to the following: given a set of intervals, find all places where there are no intervals.

        #events approach
        #for each intervla, create two enets
        #sort events
        #for each evenrt occuring at t, if balance is 0, then prev,t did ont have any intervals
        OPEN, CLOSE = 0, 1

        events = []
        for emp in schedule:
            for interval in emp:
                events.append((interval.start, OPEN))
                events.append((interval.end, CLOSE))
        
        events.sort()

        ans = []
        prev = None
        bal = 0

        for time, status in events:
            if bal == 0 and prev is not None: #what does bal mean here, means no start no end
                ans.append(Interval(prev,time))
            
            if status == OPEN:
                bal += 1
            else:
                bal -= 1
            
            prev = time
        
        return ans


