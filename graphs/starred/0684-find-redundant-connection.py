# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:


# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# # 

# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         #build adj list o(n^2)
#         graph = defaultdict(set)

#         def has_path(src, dst, visited):
#             if src == dst:
#                 return True
#             visited.add(src)
#             for neighbor in graph[src]:
#                 if neighbor not in visited:
#                     if has_path(neighbor, dst, visited):
#                         return True
#             return False

#         for u, v in edges:
#             # if path already exists between u and v
#             #1 -> 2 ->3 -> 4 vs 1 -> 4 
#             # adding this edge creates a cycle -> it's redundant
#             if has_path(u, v, set()):
#                 return [u, v]
#             graph[u].add(v)
#             graph[v].add(u)

#         return []

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # Step 1 — Build the graph
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [False] * (n + 1)
        cycle = set()
        cycleStart = -1
        # Step 2 — Find the cycle with DFS
        def dfs(node, par):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True

            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node) # this node is part of cycle
                    if node == cycleStart:
                        cycleStart = -1 #stop collecting once we in circle
                    return True
            return False

        dfs(1, -1)
            # Find the last edge in the original list where both endpoints are part of the cycle
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]

        return []
    
    #time o(n)
    #space o(n)