# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node,
#  if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2.
#  These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

# Example 1:


# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int: # type: ignore
        
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow #need to get rid of connection
            fast = fast.next.next
            slow = slow.next
        
        prev.next = None

        curr = slow
        prev = None

        #reverse
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        curr = prev
        maxTwinSum = 0

        while curr and head: #compare the reversed and head
            maxTwinSum = max(maxTwinSum, curr.val + head.val)
            curr = curr.next
            head = head.next
        
        return maxTwinSum


        

