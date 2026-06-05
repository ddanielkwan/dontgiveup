# A company is planning to interview 2n people. 
# Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti,
#  and the cost of flying the ith person to city b is bCosti.

# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

 

# Example 1:

# Input: costs = [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.

# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
# Example 2:

# Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# Output: 1859

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        def dfs(i, aCount, bCount):
            if i == len(costs):
                return 0
            if dp[aCount][bCount] != -1:
                return dp[aCount][bCount]

            res = float("inf")
            if aCount > 0:
                res = costs[i][0] + dfs(i + 1, aCount - 1, bCount)
            if bCount > 0:
                res = min(res, costs[i][1] + dfs(i + 1, aCount, bCount - 1))

            dp[aCount][bCount] = res
            return res

        return dfs(0, n, n)
    
#greedy
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        #how to determine one eprson to city a or other to city a
        #we will look at cost difference, cost of b - cost of a , means how much more expensive it is
        #to send them to city a than city b
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])

        diffs.sort()
        res = 0
        for i in range(len(diffs)):
            if i < len(diffs) // 2:
                res += diffs[i][2] #person 2 because its muhc harder to fly preson a because that would be more expensive 
            else:
                res += diffs[i][1]

        return res