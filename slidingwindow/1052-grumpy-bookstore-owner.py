# There is a bookstore owner that has a store open for n minutes. 
# You are given an integer array customers of length n 
# where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers 
# leave after the end of that minute.

# During certain minutes, the bookstore owner is grumpy. 
# You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

# When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.

# The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.

# Return the maximum number of customers that can be satisfied throughout the day.

 

# Example 1:

# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

# Output: 16

# Explanation:

# The bookstore owner keeps themselves not grumpy for the last 3 minutes.

# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

# Example 2:

# Input: customers = [1], grumpy = [0], minutes = 1

# Output: 1



class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        #1 is grumpy

        #can we use a window to determine which isthe best window that is satisfied
        #key is : not grump FOR MINUTES CONSECUTIVE
        #need disjoint

        alreadyHappy = 0

        l = 0

        notHappyToHappy = 0

        maxNotHappyToSatisfied = 0

        for r in range(len(customers)):
            if grumpy[r] == 1:
                notHappyToHappy += customers[r]
            if grumpy[r] == 0:
                alreadyHappy += customers[r]
            
            if r - l + 1 > minutes : #lets determine possible highest satisfied window using superpower
                # disjoint means a customer is counted from exactly ONE source
                # that mean maxNotHappyToSatisfied is tracking the highest grumpy to happy cusotmers
                if grumpy[l] == 1:
                    notHappyToHappy -= customers[l]
                l += 1
            
            maxNotHappyToSatisfied = max(maxNotHappyToSatisfied, notHappyToHappy)
        
        return alreadyHappy + maxNotHappyToSatisfied
            

