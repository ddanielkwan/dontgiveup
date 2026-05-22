# there are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, 
# then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, 
# you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.

 

# Example 1:


# Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
# Output: [false,true]
# Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
# Course 0 is not a prerequisite of course 1, but the opposite is true.
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #must take a before b 

        #is course u a prereq of v in queries[j]

        # res = []
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[b].append(a)
        #solution 1 -> o(q *(n+m))
        cache = {}
        def dfs(node,target):
            if node == target:
                return True
            if (node,target) in cache:
                return cache[(node,target)]
            for prereq in graph[node]:
                if dfs(prereq,target):
                    cache[(node,target)] = True
                    return cache[(node,target)]
                
            cache[(node,target)] = False
            return cache[(node,target)]
        
        for u, v in queries:
            res.append(dfs(v, u))
        return res

        #solu 2 dfs reutnr hashset of all prereq for acourse
        #so upper parent can append all those as prerequ

        prereqMap = {}

        def dfs(course):
            if course not in prereqMap:
                prereqMap[course] = set()
                for prereq in graph[course]:
                    #union two sets
                    prereqMap[course] = prereqMap[course] | dfs(prereq)
                prereqMap[course].add(course)

            return prereqMap[course]
        for c in range(numCourses):
            dfs(c)

        for u, v in queries:
            res.append(u in prereqMap[v])
        return res


