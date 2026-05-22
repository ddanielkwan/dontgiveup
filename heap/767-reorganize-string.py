# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""


import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        

        f = Counter(s)

        prev = None #keep track of previous word
        heap = [(-c, char) for char, c in f.items()]
        heapq.heapify(heap) #makes sense to always process highest freq number first 

        res = ""

        while prev or heap: 
            # still have a character we need to place but there are no other characters left in the heap so we have no alternative character to separate it
            if prev and not heap:
                return ""

            count, char = heapq.heappop(heap)
            count += 1 #+1 means process since negative

            if prev:
                #well never have duplicate b in prev and b in heap since its a counter
                heapq.heappush(heap, prev)
            
            res += char
            if count < 0 :
                #do we still have count after +1 ? 
                prev = (count, char)
            else:
                prev = None
        return res


