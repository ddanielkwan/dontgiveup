# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
#         candidates.sort()
#         subset = []
#         res = []

#         def backtrack(i,currentsum):
#             if currentsum == target:
#                 res.append(subset.copy())
#                 return
            
#             if i >= len(candidates) or currentsum > target:
#                 return
#             # Decision 1: Include candidates[i]
#             subset.append(candidates[i])
#             backtrack(i+1, currentsum+candidates[i]) 
#             subset.pop() #cleanup
#             #  The decision to include happened when you appended and calledbacktrack
#             # Decision 2: Exclude candidates[i] and all its duplicates
#             #now check if currnet index same as previous and move pointter
#             i += 1
#             while i < len(candidates) and candidates[i-1] == candidates[i]:
#                 i += 1
#             backtrack(i, currentsum) #do not include
        
#         backtrack(0,0)
#         return res



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        subset = []
        res = []

        def bt(i):
            if len(subset) == k:
                res.append(subset.copy())
                return
            
            if i > n :
                return
            
            subset.append(i)
            bt(i+1)
            subset.pop()
            bt(i+1)
        bt(1)
        return res

