# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

# Example 1:


# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #prims alogritmh simialr to djistraks we use min heap
        #but this time we introduce frontier conecpt
        #for each iteration(node), we calculate the distance and append to minheap
        #keep popping minheap, o(n^2 log n)

        n = len(points)

        adj = {i:[] for i in range(len(points))} #each (cost, neighbour node)
        for i in range(n):#for every point, compare it every other point in graph
            x1, y1 = points[i]
            for j in range(i+1, n):
                #calculate distance
                x2,y2 = points[j]

                #manhattan dis
                dist = abs(x1-x2) + abs(y1-y2)
            
                adj[i].append([dist,j])
                adj[j].append([dist,i])
            
            
        res = 0
        visit = set()
        minHeap = [[0,0]] #cost and point

        while len(visit) < n:
            c, p = heapq.heappop(minHeap)

            if p in visit:
                continue
            
            visit.add(p)
            res += c

            for neighcost, neigh in adj[p]:
                if neigh not in visit:
                    heapq.heappush(minHeap,[neighcost, neigh])
            
        return res

