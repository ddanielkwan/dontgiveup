
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

# Example 1:

# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
# Example 2:

# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        #integer n number of nodes in directed 0-n-1
        #edge red or blue
        #rededges blue edges
        #[a,b] a to b red edge

        #return asnwer[x] of len n, each asnwer is length of shortest path from 0 to that node
        #shortest path : bfs

        red = defaultdict(list)
        blue = defaultdict(list)

        for src, dst in redEdges:
            red[src].append(dst)
        
        for src, dst in blueEdges:
            blue[src].append(dst)
        
        ans = [-1 for _ in range(n)]

        ans[0] = 0 #always 0
        visted = set()

        q = deque()
        q.append((0, 0, None)) #node, distancetook to get here, prevcolor
        visited = set()
        visited.add((0,None)) #node, color came from

        while q :
            node, distance, prevcolor = q.popleft()

            if ans[node] == -1:
                #if first time visiting this means we found the shortest path
                ans[node] = distance
            
            if prevcolor != "RED": #if its not red use blue and alternate
                for nei in red[node]:
                    if (nei,"RED") not in visited:
                        visited.add((nei,"RED"))
                        q.append([nei,distance +1,"RED"])
            if prevcolor != "BLUE": #if its not red use blue and alternate
                for nei in blue[node]:
                    if (nei,"BLUE") not in visited:
                        visited.add((nei,"BLUE"))
                        q.append([nei,distance +1,"BLUE"])
            
        return ans