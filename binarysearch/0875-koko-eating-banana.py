# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
#  If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        def canFinish(k):
            usedHours = 0
            for pile in piles:
                if pile <= k:
                    usedHours += 1
                else:
                    usedHours += math.ceil(pile/k) #if a pile is 10 and k is 3 , she needs 1(3) + 1(3) + 1(3) + 1(1) hours
            
            if usedHours <= h:
                return True
            return False

        l = 1

        r = max(piles)

        minimumK = max(piles)

        while l <= r :

            k = l + (r-l)//2

            canFinishPile = canFinish(k)

            if not canFinishPile:
                l = k + 1
            else:
                minimumK = k
                r = k - 1
        
        return minimumK


# Binary search doesn’t require l to always be valid —
# it requires the invariant to hold
# Something that is ALWAYS true every time the loop runs
# class Solution:
    # def minEatingSpeed(self, piles: list[int], h: int) -> int:
    #     l = 1 
    #     r = max(piles)


    #     while l <=r :
    #         k = l +(r-l)//2

    #         t = 0

    #         for p in piles:
    #             t += math.ceil(p/k)
    #         if t > h:
    #             l = k + 1
    #         else:
    #             r =k - 1
    #     return l



