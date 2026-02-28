# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

 

# Example 1:


# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #n cities 0 - n - 1
        #n-1 roads
        #roads are in connections [a,b] a -> b

        #tells us there is no loops because n -1 roads, and tells us graph is connected
        #lets first check all of neighoburs of 0, if they can reach 0,
        #and then check neighobburs of thos eneighbours that can reach them

        edges = {(a,b) for a,b in connections} #we wnat to know instantly if city a can reach city b so thats why we have a set

        visited = set()

        graph = defaultdict(list)

        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        roadsChanged = 0
        def dfs(node):
            nonlocal roadsChanged

            visited.add(node)
            for neighbour in graph[node]:
                #determine if there is an edge from that neighbour to current node
                if neighbour not in visited:
                    if (neighbour, node) not in edges:
                        roadsChanged += 1
                    dfs(neighbour)


        dfs(0) #start at city 0 to check neighbours and recursively check their neighbours
        return roadsChanged

