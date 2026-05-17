# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

 

# Example 1:

# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10

# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        #within days

        #weight
        #ship will have some capacity which can hold a chunk of weights
        #goal is to choose a capacity of the ship 
        #such that it is the minimal capacity that we need to carry all of the weights
        #think about it in number of ships make more sense
        #we are given days = ships
        #lets try capacity = 1, with [1,2,3,4,5] cant because the second ship acnt even hold 2
        #so minimum hast o be astleat the max ofthe array
        #upperbound would never be higher than total sum of array
        #[5, 15] do a binary search on this search space
        #so becomes m = 10 and then try to minimize again r = 10
        #now m = 7 , does not work, but now we have to increase search space
        # l = 7 + 1 = 8


        l = max(weights)
        r = sum(weights)

        while l <= r :

            capacity = l + (r-l)//2

            capacityLeft = capacity
            daysTaken = 1

            for weight in weights:
                if capacityLeft - weight < 0 :
                    daysTaken += 1
                    capacityLeft = capacity

                capacityLeft -= weight
            


            if daysTaken > days:
                l = capacity + 1
            else:
                r = capacity - 1
        
        return l

     

