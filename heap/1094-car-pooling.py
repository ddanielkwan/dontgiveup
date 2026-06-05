# There is a car with capacity empty seats. 
# The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates
#  that the ith trip has numPassengersi passengers and the locations to 
# pick them up and drop them off are fromi and toi respectively. 
# The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

# Example 1:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# Example 2:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        


        #capacity
        #drives east

        #trips[i] = numpassengers, from, to

        currentCapacity = 0

        trips = sorted(trips, key = lambda x:x[1]) #sort by time start
        minheap = [] #to, source, numpassengers
        #we will need a minheap to track the earliest end times, this will tell us when to pop and remove these passengers
        #intution we are storing the min values
        
        for numpassengers, source, to in trips:
            currentCapacity += numpassengers

            while minheap and minheap[0][0] <= source: #theyve arrived
                _, _, passengers = heapq.heappop(minheap)
                currentCapacity -= passengers
            
            if currentCapacity > capacity:
                return False
            
            heapq.heappush(minheap,(to,source,numpassengers))
        
        return True

