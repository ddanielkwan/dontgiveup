# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.


# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #total numcourses have to take
        #0 to numcourses -1
        #prereq = [a,b] must take b first if take a 

        #true if can finissh all coruses
        #assert no cycle

        prereqs = defaultdict(list)

        for a ,b in prerequisites:
            prereqs[a].append(b)
        
        seen = set() #this is to store what courses we seen and evaluated as true already
        cycle = set() #this is to track the current course' dfs flow

        def dfs(course):
            if course in cycle:
                return False
            if course in seen:
                return True
            cycle.add(course)
            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False
            
            seen.add(course)
            cycle.remove(course)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False #if any of coruses cant be completed reutrn flase
        
        return True

