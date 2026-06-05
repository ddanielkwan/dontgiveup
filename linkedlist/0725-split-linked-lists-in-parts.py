# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. 
# This may lead to some parts being null.

# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater
#  than or equal to parts occurring later.

# Return an array of the k parts.

 

# Example 1:


# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        #algorithm
        #determine the total length
        #determine the base length for each array spot by length // k
        # the remainder length % k

        #loop for k
        #iterate through curr pointer for b base amount + 1 if there is remainder left
        #decrement remainder
        #make sure to cut off the tail and set curr as curr.next
        
        length = 0
        curr = head

        while curr :
            length += 1
            curr = curr.next
        
        baseLength = length // k #this determine the min that all will have 
        #[[1],[2],[],[]] base length is 0

        remainder = length % k 

        curr = head

        res = []

        for i in range(k):
            res.append(curr)
            #baselength - 1 because N - 1 times we alreaddy appended curr
            for j in range(baseLength - 1 + (1 if remainder != 0 else 0)):
                if not curr:
                    break
                
                curr = curr.next
            remainder -= (1 if remainder else 0) #how many more parts stil need an extra node, 
            
            if curr:
                 #disconnect and then go next
                curr.next, curr = None, curr.next
        
        return res
        

