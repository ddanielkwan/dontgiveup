# A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

# Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

# The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

# Return the number of minutes needed to inform all the employees about the urgent news.

 

# Example 1:

# Input: n = 1, headID = 0, manager = [-1], informTime = [0]
# Output: 0
# Explanation: The head of the company is the only employee in the company.

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        #tree structure where at each level going down is employee

        #need to establish tree first

        graph = defaultdict(list) #adjacency list

        for employeeId, mng in enumerate(manager): #index is employeeId
            if manager != -1:
                graph[mng].append(employeeId)
            
        #inform time is time it takes to infrom all of its subordinates
        q = deque()
        q.append((headID, informTime[headID]))

        res = 0
        #the time needed, is always based on the slowest time needed to ifnrom all
        #slowest here is max time
        while q :
            mng, t = q.popleft()
            res = max(res, t)

            for associate in graph[mng]:
                #if its a manager, we need to get the time it takes for them to inform
                q.append((associate, t + informTime[associate]))
        
        return res