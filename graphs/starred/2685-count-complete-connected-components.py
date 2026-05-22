# You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1.
# You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

# Return the number of complete connected components of the graph.

# A connected component is a subgraph of a graph in which there exists a path between any two vertices, 
# and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

# A connected component is said to be complete if there exists an edge between every pair of its vertices.

 
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        #given int n
        #undirect graph n nodes
        #edges a,b 

        #complete every node has edge to every other node

        #first phase just split the nodes
        #run a dfs from every node to get a component

        #second phase, count edges and detemrine if componenet valid or not
        #compare number of node to number of edges
        #if 3 nodes, theres 2 edges going out of it
        #if 4 node stheres 3 edges going out of it 
        #so its that number - 1

        adj = defaultdict(list)
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        def dfs(v, res): #just collect all vertex
            if v in visit:
                return res
            visit.add(v)
            res.append(v)
            for nei in adj[v]:
                dfs(nei,res)
            return res
        
        res = 0
        visit = set()
        for v in range(n):
            if v in visit:
                continue
            component = dfs(v, []) #this array will be all of the nodes that belong to the one belong to this node
            flag = True
            for v2 in component:
                #all vertiices in there
                if len(component) - 1 != len(adj[v2]): #to len of edges connected to v2 
                    flag = False
                    break
            if flag:
                res += 1


        return res

