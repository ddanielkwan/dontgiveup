# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        # a/b = 2 b/c = 3
        # b = 2a b = 3c
        # 2a = 3c
        # a/c = 6 

        #if we look for a/b , we then need ot look for b where b is in numerator spot , so node so the denominator can eventually cancel out
        #e.g start at a
        #map numerator to donminators ,m ultuple the values a/b x b/c put values ofthhese as theedges so 2 x 3 multiple all the edges
        #we can also map demonitaors to numerator but how make sense a/b x b/c = 6 and c/b x b/a = 6, so we ned to take the inverse when we go in reverse order


        adj = defaultdict(list) #map numerator a to [b, a/b]
        for i, eq in enumerate(equations):
            a,b = eq
            adj[a].append((b, values[i])) #forward
            adj[b].append((a, 1/values[i])) #backwards inverse

        #a/b src = a , path starting at a and get to b and multiple weiht of all edges
        def bfs(src, target):
            if src not in adj or target not in adj: #[x,x ] does not exist [z,b] z does not exist
                return -1
            q, visit = deque(), set()
            q.append([src, 1]) #second vlue is the multiplication

            visit.add(src)
            while q :
                node, weight = q.popleft()

                if node == target:
                    #multiplciation up umtil this node
                    return weight
                for nei, w in adj[node]:
                    if nei not in visit:
                        q.append((nei, w * weight))
                        visit.add(nei)
            return -1

        #update as of may 2026
        #intution:
        #a/b = 2 , b/c = 3

        #what is a/c ?

        #treat each letter as node
        #a -> b
        #edge here is 2
        #b -> c edge here is 3

        #a/b x b/c => 2x3

        #from a 2-> b 3-> c each move we multiply the edge
        #so a-b-c = 6 

        #now backwards if c-b-a ? divide 1/value

        return [bfs(q[0],q[1]) for q in queries]




