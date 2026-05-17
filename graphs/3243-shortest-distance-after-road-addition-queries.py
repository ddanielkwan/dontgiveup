# You are given an integer n and a 2D integer array queries.

# There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

# queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

# Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

 

# Example 1:

# Input: n = 5, queries = [[2,4],[0,2],[0,4]]

# Output: [3,2,1]

# Explanation:



# After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.



# After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.



# After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        #run bfs or dfs everytime thers new query
        #q x (n+q)


        adj = []
        for i in range(n):
            adj.append([i+1])

        def shortest_path(): #we always start 0 and to n-1
            q = deque()
            q.append((0,0)) #node, length took to reach that node
            visit = set()
            visit.add((0))
            while q :
                node, length = q.popleft()
                if node == n-1:
                    return length
                
                for nei in adj[node]:
                    if nei not in visit:
                        q.append((nei, length+1))
                        visit.add(nei)
            

        
        res = []
        for src,dst  in queries:
            adj[src].append(dst)
            res.append(shortest_path())
        
        return res

