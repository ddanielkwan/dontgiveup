# There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
# The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, 
# meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges.
#  A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

 

# Example 1:

# Illustration of graph
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #directed graph
        #0 - n-1 nodes
        #graph[i] is node adjacent to i

        #terinal node if no outgoing edges
        #safe node if every possibel path from this node leads to terminal node or another safe node

        #find all safe nodes of the graph
        #sorted in ascending

        #graph[0] 1 ,2  means 0 > 1 , 0 > 2

        res = []
        safenodes = {}
        def dfs(node):
            if graph[node] == []: #terminal node
                return True
            
            if node in safenodes:
                return safenodes[node] #already computed no need to recompute true or false
            
            safenodes[node] = False
            for nextnode in graph[node]:
                if not dfs(nextnode):
                    return False #not a safe node
            
            safenodes[node] = True
            return True
            

        for n in range(len(graph)):
            if dfs(n): #if the node is safe
                res.append(n)

        return res


