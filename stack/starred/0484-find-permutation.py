# A permutation perm of n integers of all the integers in the range [1, n] can be represented as a string s of length n - 1 where:

# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the lexicographically smallest permutation perm and return it.

 

# Example 1:

# Input: s = "I"
# Output: [1,2]
# Explanation: [1,2] is the only legal permutation that can represented by s, where the number 1 and 2 construct an increasing relationship.
# Example 2:

# Input: s = "DI"
# Output: [2,1,3]
# Explanation: Both [2,1,3] and [3,1,2] can be represented as "DI", but since we want to find the smallest lexicographical permutation, you should return [2,1,3]



class Solution:
    def findPermutation(self, s: str) -> List[int]:
        # s[i] == 'I' if perm[i] < perm[i + 1], and

        #i means increasing

# s[i] == 'D' if perm[i] > perm[i + 1] d means decrasing

        # You want the lexicographically smallest permutation, so you want to place the smallest numbers as early as possible

        #if IDDI
        #means [1,5]

        #we try 1 , 2,3 , 4,5
        #we we see D means we reverse 
        #D is at index [1:2]
        #we need to reverese 3 elements
        # [1, 4 , 3 , 2, 5]

        # perm = list(range(1, len(s) + 2))

        # i = 0

        # while i < len(s):

        #     if s[i] == "D":

        #         start = i

        #         while i < len(s) and s[i] == "D":
        #             i += 1

        #         perm[start:i+1] = reversed(perm[start:i+1])

        #     else:
        #         i += 1

        # return perm

        #cracked
        #stack order is reverse naturally

        #if you see i you can just pop becaue its in order
        #if you see D, dont do anything,
        #use LIFO property
        stack = []
        result = []
        # s = "IDDI"
        for i in range(len(s) + 1): #[1,n]
        
            stack.append(i + 1) 

            if i == len(s) or s[i] == "I":

                while stack:
                    result.append(stack.pop())

        return result