# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
 
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        inbound = defaultdict(int)
        outbound = defaultdict(int)

        for a, b in trust:
            inbound[b] += 1
            outbound[a] += 1
        #people labeled 1-n
        for person in range(1, n+1):
            #if that person has n-1 people trusting him and doesnt trust anyone
            #they are the town judge
            if inbound[person] == n-1 and outbound[person] == 0:
                return person
        
        return -1