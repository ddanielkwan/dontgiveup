# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        
        # prev will point to the previous node in the reversed list
        # Initially, there is no previous node
        prev = None
        
        # curr starts at the head of the original list
        curr = head

        # Traverse the linked list until we reach the end
        while curr:
            
            # Step 1: Save the next node
            # We must save it before changing curr.next,
            # otherwise we lose access to the rest of the list
            tmp = curr.next
            
            # Step 2: Reverse the pointer
            # Make current node point backward instead of forward
            curr.next = prev
            
            # Step 3: Move prev forward
            # prev now becomes the current node
            prev = curr
            
            # Step 4: Move curr forward
            # Continue traversal using the saved next node
            curr = tmp
        
        # At the end:
        # - curr is None (we reached the end)
        # - prev is the new head of the reversed list
        return prev

