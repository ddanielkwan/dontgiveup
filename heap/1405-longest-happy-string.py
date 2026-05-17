# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer


import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        

        res = ""
        
        #  use a max heap to always pick the character
        # with the largest remaining frequency.

        maxHeap = []

        # Push (negative_count, character) into heap
        # Example: if a = 3 → push (-3, 'a')
        # We skip if count is 0 because no need to store it
        for count, char in [(-a,'a'), (-b,'b'), (-c,'c')]:
            if count != 0:
                heapq.heappush(maxHeap, (count,char))
        

        while maxHeap:
            
            # always try to use the character with highest remaining frequency

            count, char = heapq.heappop(maxHeap)

            # Check if adding this character would create "xxx"
            # We only need to check last two characters
            if len(res) > 1 and res[-1] == res[-2] == char:
                
                # If we cannot use this char and there is no other choice,
                # then we cannot continue building a valid string
                if not maxHeap:
                    break

                # otherwse, use the second most frequent character instead
                count2, char2 = heapq.heappop(maxHeap)

                res += char2
                count2 += 1

                # if there are still occurrences left, push back into heap
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))

                # IMPORTANT:
                # We did NOT use the first character,
                # so we must push it back unchanged
                heapq.heappush(maxHeap, (count, char))

            else:
                # If it is safe to use this character,
                # append it to the result
                res += char
                count += 1

                # If there are still remaining occurrences,
                # push back into heap
                if count:
                    heapq.heappush(maxHeap, (count,char))
        

        return res

