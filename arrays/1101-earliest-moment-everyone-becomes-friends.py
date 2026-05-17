# There are n people in a social group labeled from 0 to n - 1.
#  You are given an array logs where logs[i] = [timestampi, xi, yi] 
# indicates that xi and yi will be friends at the time timestampi.

# Friendship is symmetric. That means if a is friends with b, 
# then b is friends with a. Also, person a is acquainted with a person b 
# if a is friends with b, or a is a friend of someone acquainted with b.

# Return the earliest time for which every person became acquainted with 
# every other person. If there is no such earliest time, return -1.

 

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        #intution ; People become fully connected gradually over time.
        logs = sorted(logs, key=lambda x:x[0])

        graph = defaultdict(set)

        for i in range(n):
            graph[i] = {i}
        #build graph as we are going
        for ts, p1, p2 in logs:
            #p1 will get all acquaintces with p2
            graph[p1] = graph[p1] | graph[p2]

            for p3 in graph[p1]:
                graph[p3] = graph[p3] | graph[p1]
            
            if len(graph[p1]) == n:
                return ts
        
        return -1
        #o(mlogm sorted + union n * m )
        #space sorting in python is o(m)

