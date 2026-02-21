# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

# Choose the pile with the maximum number of gifts.
# If there is more than one pile with the maximum number of gifts, choose any.
# Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile.
# Return the number of gifts remaining after k seconds.

 

# Example 1:

# Input: gifts = [25,64,9,4,100], k = 4
# Output: 29
# Explanation: 
# The gifts are taken in the following way:
# - In the first second, the last pile is chosen and 10 gifts are left behind.
# - Then the second pile is chosen and 8 gifts are left behind.
# - After that the first pile is chosen and 5 gifts are left behind.
# - Finally, the last pile is chosen again and 3 gifts are left behind.
# The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        # we need max heap because we want the maximum everytime, defutl is min heap
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        while k:
            k -= 1

            largest = -heapq.heappop(gifts)   # get largest
            # reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile
            reduced = int(math.sqrt(largest))

            heapq.heappush(gifts, -reduced)   # put back

        return -sum(gifts)
