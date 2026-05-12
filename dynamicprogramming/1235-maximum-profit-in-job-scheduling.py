# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

# Example 1:



# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job. 
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        #brute force bcak tracking + memo
        #look at intervals, probably makes sense to sort by start time
        #greedy won work here because there can be overalpping jobs with higther profit, wont know
        #subproblems

        intervals = sorted(zip(startTime,endTime,profit))

        cache = {}
        def dfs(i):
            if i == len(intervals):
                #no profit remaining
                return 0
            
            if i in cache:
                return cache[i]
            
            #dont include
            res = dfs(i+1)

            #include
            j = i + 1
            while j < len(intervals):
                #trying to fidn te max for overlapping intevvals
                #because we can only do 1 job
                #we can optimize with binary search
                if intervals[i][1] <= intervals[j][0]: #if end time of current interval is less than start time of new interval (find where these overlapping inntervals end)
                    break
                j += 1
            cache[i] = max(res, intervals[i][2] + dfs(j))
            return cache[i]
        
        return dfs(0)
    


    class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        #brute force bcak tracking + memo
        #look at intervals, probably makes sense to sort by start time
        #greedy won work here because there can be overalpping jobs with higther profit, wont know
        #subproblems

        intervals = sorted(zip(startTime,endTime,profit))

        cache = {}
        def dfs(i):
            if i == len(intervals):
                #no profit remaining
                return 0
            
            if i in cache:
                return cache[i]
            
            #dont include
            res = dfs(i+1)

            #include
            # j = i + 1
            # while j < len(intervals):
                #trying to fidn te max for overlapping intevvals
                #because we can only do 1 job
                #we can optimize with binary search
                # if intervals[i][1] <= intervals[j][0]: #if end time of current interval is less than start time of new interval (find where these overlapping inntervals end)
                #     break
                # j += 1
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            cache[i] = max(res, intervals[i][2] + dfs(j))
            return cache[i]
        
        return dfs(0)