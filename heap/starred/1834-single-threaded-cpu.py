# You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

# You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

# If the CPU is idle and there are no available tasks to process, the CPU remains idle.
# If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
# Once a task is started, the CPU will process the entire task without stopping.
# The CPU can finish a task then start a new one instantly.
# Return the order in which the CPU will process the tasks.

 

# Example 1:

# Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
# Output: [0,2,3,1]
# Explanation: The events go as follows: 
# - At time = 1, task 0 is available to process. Available tasks = {0}.
# - Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
# - At time = 2, task 1 is available to process. Available tasks = {1}.
# - At time = 3, task 2 is available to process. Available tasks = {1, 2}.
# - Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
# - At time = 4, task 3 is available to process. Available tasks = {1, 3}.
# - At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
# - At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
# - At time = 10, the CPU finishes task 1 and becomes idle.


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #n tasks 0 to n-1
        #tasks[i] = enq, procestime
        #ith task is availabe to process at *enq time or later
        #processing time to finish
        #only do 1 task at a time
        #if idle and time is before any enque time just idle

        #step1 sort by enq time amnd get index
        for index, val in enumerate(tasks):
            val.append(index)
        tasks.sort(key=lambda x : x[0]) 




        minheap = [] #store (processingTime, index) #we want to get fastest processing always
        orderOfTasksProcessed = []

        i = 0
        time = tasks[0][0] #first task time to start

        while minheap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time : #time greater than enqu means tasks is available to prorcess
                heapq.heappush(minheap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if not minheap: #if no avaialble task, cpu is idle so fast forward
                time = tasks[i][0]
            
            else:
                processingTime, taskIndex = heapq.heappop(minheap) 
                time += processingTime
                orderOfTasksProcessed.append(taskIndex)
        
        return orderOfTasksProcessed



