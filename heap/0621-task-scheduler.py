# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
# Each CPU interval can be idle or allow the completion of one task. 
# Tasks can be completed in any order, but there's a constraint: 
# there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

 

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2

# Output: 8

# Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

# After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

# Example 2:

# Input: tasks = ["A","C","A","B","D","B"], n = 1

# Output: 6

# Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

# With a cooling interval of 1, you can repeat a task after just one other task


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        #use a max heap to always pick the task with the most remaining work
        maxHeap = [-freq for freq in count.values()] 

        heapq.heapify(maxHeap)
        # Queue to store tasks that are "cooling down"
        # Each item = [remaining_count, time_when_it_can_be_used_again]

        q = deque()

        t = 0

        while q or maxHeap:
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1 #add one closer to 0 so means we processed

                if count < 0:# still available
                    q.append([count, t + n]) #after we processed and its still avaialble we add to queue for cooldown
                
            while q and q[0][1] <= t: #get all items in q that are ready to processed <= t and add them back to heap
                count, _ = q.popleft()
                heapq.heappush(maxHeap, count)
            t += 1
        
        return t 


