# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

 

# Example 1:


# Input: bombs = [[2,1,3],[6,1,4]]
# Output: 2
# Explanation:
# The above figure shows the positions and ranges of the 2 bombs.
# If we detonate the left bomb, the right bomb will not be affected.
# But if we detonate the right bomb, both bombs will be detonated.
# So the maximum bombs that can be detonated is max(1, 2) = 2.


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #bombs[i] = [x,y,r]
        #recall dsitance = d^2 = x^2 + y^2
        edges = defaultdict(list)
        #build our graph 
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)): #this loop because we see if each point or "node" can reach each other
                x1, y1 , r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                d = sqrt((x1-x2)**2 + (y1-y2)**2)
                #radius is how far it can reach
                #distance is distance between two center nodes
                #if radius expands at least that dsitance, then it can reach that node
                if r1 >= d:
                    edges[i].append(j)
                if r2 >= d:
                    edges[j].append(i)
        
        maxbombs = 0

        def dfs(bomb): #dfs to caclulate how many of bombs this bomb can detonate recursively
            nonlocal maxbombs

            res = 0
            if bomb in visited:
                return 0
            visited.add(bomb)
            for adjbomb in edges[bomb]:
                if adjbomb not in visited:
                    res += dfs(adjbomb) + 1
            maxbombs = max(maxbombs,res)
            return res
            


        for i in range(len(bombs)):
            visited = set()
            dfs(i)
        
        return maxbombs + 1



