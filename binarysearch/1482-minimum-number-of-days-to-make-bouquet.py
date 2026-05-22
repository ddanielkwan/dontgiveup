# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. 
# If it is impossible to make m bouquets return -1.

 

# Example 1:

# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        #bloomday i = days to bloom for i flower
        #how manydays need ot wait to make m bouquet
        #k is adjacent flower

        # Key observation
        # If you can make m bouquets on day x:
        # then you can ALSO make them on any later day
        # because more flowers bloom over time.
        # That means the answer is monotonic:
        # FFFFFTTTTT
        # So binary search works
        n = len(bloomDay)

        if m * k > n:
            return -1

        def can_make(day):

            bouquets = 0
            flowers = 0

            for bloom in bloomDay:

                if bloom <= day:
                    flowers += 1

                    if flowers == k: #consecutive flowers
                        bouquets += 1
                        flowers = 0

                else:
                    flowers = 0

            return bouquets >= m

        left = min(bloomDay) #What is the earliest possible day ANY flower exists?
        right = max(bloomDay) #latest day , wrose case

        res = -1

        while left <= right:

            mid = (left + right) // 2

            if can_make(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res

