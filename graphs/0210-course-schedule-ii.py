# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:

# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #prereq to take a need b first


        prereq = defaultdict(list)

        for a, b in prerequisites:
            prereq[a].append(b)
        
        #return ordering 

        res = []

        cache = {} #courses we evaluated before and set to true

        cycle = set() #cycle of current eval flow

        def dfs(course): #returns true or false evaluated but also add to res in order
            if course in cache:
                return True
            if course in cycle:
                return False #cant cycle
            
            cycle.add(course)
            for prq in prereq[course]:
                if not dfs(prq):
                    return False
            #kim possible
            cycle.remove(course)
            cache[course] = True
            res.append(course)
            return True

        for n in range(numCourses):
            if not dfs(n): #if any of them no possible then return empty
                return [] 
        
        return res