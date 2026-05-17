# You are given an array people where people[i] is the weight of the ith person, 
# and an infinite number of boats where each boat can carry a maximum weight of limit. 
# Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

 

# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        #intuition: greedy approach
        # Each boat can take at most 2 people, and the total weight ≤ limit
        # So for every boat, use its capacity as efficiently as possible

        #Always try to pair the lightest person with the heaviest person
        # heaviest person is the hardest to place
        #if the heaviest person can’t share a boat with the lightest, then
        #they cannot share with anyone else either so the heaviest must go alone


        people.sort() #sort ascending weight
        #indices
        lightest = 0
        heaviest = len(people) - 1

        boatsRequired = 0

        while lightest <= heaviest :
            if people[heaviest] + people[lightest] <= limit:
                lightest += 1
            
            heaviest -= 1
            boatsRequired += 1 #our boat increases anyways we have unlimited boats, we just fit lightest person, if they fit
        
        return boatsRequired
        



        

