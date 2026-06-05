# You are given a list of airline tickets where tickets[i] = [fromi, toi] 
# represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus,
#  the itinerary must begin with "JFK". If there are multiple valid itineraries, 
# you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

# Example 1:


# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Key Insight: Create Adjacency Map of Defaultdict<MinHeap> to keep lexical order
        #Post order dfs to avoid being trapped

        airportMap = defaultdict(list)
        for frm, to in tickets:
            heapq.heappush(airportMap[frm], to)
        
        route = []
        def dfs(airport):
            while airportMap[airport]:
                next_airport = heapq.heappop(airportMap[airport])
                dfs(next_airport)
            route.append(airport)
        dfs("JFK")
        return route[::-1]