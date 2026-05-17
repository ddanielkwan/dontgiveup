# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #brute force back tracking

        #create every sginelpossiblre way to partition 
        #create every single partition, dont worry about the append for now
        #focus on
        #partition
        # / | \
        #a  aa aab <- this one not a palindrome so stop
        #.  |
        res =[]
        part = []
        def dfs(index):
            if index >= len(s):
                res.append(part.copy())
                return #because we reached last index
            
            for j in range(index,len(s)):
                if self.ispali(s, index, j ):
                    part.append(s[index:j+1])
                    dfs(j + 1)
                    part.pop()

            
        dfs(0)
        return res

    def ispali(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -= 1
        return True

    

