# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        subset = []
        res = []

        def backtrack(i,currentsum):
            if currentsum == target:
                res.append(subset.copy())
                return
            
            if i >= len(candidates) or currentsum > target:
                return
            # Decision 1: Include candidates[i]
            subset.append(candidates[i])
            backtrack(i+1, currentsum+candidates[i]) 
            subset.pop() #cleanup
            #  The decision to include happened when you appended and calledbacktrack
            # Decision 2: Exclude candidates[i] and all its duplicates
            #now check if currnet index same as previous and move pointter
            i += 1
            while i < len(candidates) and candidates[i-1] == candidates[i]:
                i += 1
            backtrack(i, currentsum) #do not include
        
        backtrack(0,0)
        return res

