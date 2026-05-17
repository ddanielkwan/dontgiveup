# There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.

# You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.

# A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.

# Team a will be the champion of the tournament if there is no team b that is stronger than team a.

# Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.

# Notes

# A cycle is a series of nodes a1, a2, ..., an, an+1 such that node a1 is the same node as node an+1, the nodes a1, a2, ..., an are distinct, and there is a directed edge from the node ai to node ai+1 for every i in the range [1, n].
# A DAG is a directed graph that does not have any cycle.
 

# Example 1:



# Input: n = 3, edges = [[0,1],[1,2]]
# Output: 0
# Explanation: Team 1 is weaker than team 0. Team 2 is weaker than team 1. So the champion is team 0.


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        #n teams 0 -> n-1
        #dag

        #n int
        #edges 2d

        #edges[i] = [u, v]
        #u -> v 

        #a -> b means team a is stornger than b 
        #a is champino if no b stronger than a

        #return if unique chmapion else -1

        adj = defaultdict(int)

        for a, b in edges:
            adj[b] += 1
        champions = []

        for i in range(0, n):
            if not adj[i]:
                champions.append(i)
        
        if len(champions) > 1:
            return -1
        
        return champions[0]

