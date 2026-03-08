# You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

# You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

# Return the minimum time taken to repair all the cars.

# Note: All the mechanics can repair the cars simultaneously.

 

# Example 1:

# Input: ranks = [4,2,3,1], cars = 10
# Output: 16
# Explanation: 
# - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
# - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
# - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
# - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
# It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​


from math import sqrt


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        
        # Helper function:
        # Given a certain amount of time,
        # return how many cars each mechanics can repair
        def count_repaired(time):
            count = 0  # total cars repaired in "time"
            

            for rank in ranks:
                # From formula: time = rank * n^2
                # Solve for n: n = sqrt(time / rank)
                # We floor it because mechanic can only repair whole cars
                count += int(sqrt(time / rank))
            
            return count
        
        # Left boundary:
        # Minimum possible time (can't be 0 because no cars get repaired)
        l = 1
        
        # Right boundary (worst case):
        # Fastest mechanic (smallest rank) repairs ALL cars
        # time = rank * cars^2
        #fastst is the min
        r = min(ranks) * cars * cars
        

        res = -1
        

        while l <= r:
            

            m = (l + r) // 2
            
            # How many cars can be repaired in m time?
            repaired = count_repaired(m)
            
            # If we can repair enough cars (or more),
            # m is a valid answer, but maybe not the minimum
            if repaired >= cars:
                res = m          # record current valid time
                r = m - 1        # try to find smaller valid time
            else:
                # Not enough cars repaired -> need more time
                l = m + 1
        

        return res
