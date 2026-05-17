# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

 

# Example 1:

# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# Example 2:

# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        #simialr to house robber ,sicen you cant rob adjactent
        #remove duplicates and sort
        
        # earn2 = best earnings including current or previous numbers
# earn1 = best earnings ONE step behind earn2
        earn1 = 0
        earn2 = 0

        for i in range(len(nums)):
            curEarn = nums[i] * freq[nums[i]]
            #cant use curearn and earn2
            if i >0 and nums[i] == nums[i-1] + 1: #if current is 4 , then previosu is 3 
                temp = earn2

                earn2 = max(curEarn + earn1, earn2) 
                # e1e2
                # 1,2,3 <- earn3 being calculated if we choose 3 we cacnt choose 2 so curearn + earn1
                earn1 = temp

            else:
                #we can use both
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
        return earn2
    
#     nums = [1, 2, 3, 4]

# after processing 1:  earn1=0, earn2=1
# after processing 2:  earn1=1, earn2=2
# after processing 3:  earn1=2, earn2=4
#                                ↑
#                          this already knows
#                          everything about 1 and 2
#                          you dont need them anymore
# When you're at 4, asking "what happened at 1?" — you don't need to. earn2 already accounted for it.

