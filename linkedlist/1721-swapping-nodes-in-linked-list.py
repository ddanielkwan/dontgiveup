
# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning 
# and the kth node from the end (the list is 1-indexed).

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: # type: ignore
        
        fast = head

        for _ in range(k-1):
            fast = fast.next
        
        first = fast

        slow = head

        while fast and fast.next:
            # We want slow to land exactly on the k-th node from the end
            fast= fast.next
            slow = slow.next

        

        slow.val , first.val = first.val, slow.val
        return head

