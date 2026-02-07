# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.

 

# Example 1:


# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        
        #reverse and then compare
        # After reversing, "right" becomes "left",
        # making the comparison easy in one pass

        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # after reversal:
        # prev now points to the NEW HEAD of the reversed list
        newHead = prev

        #  dummy is a traversal pointer
        # We will move dummy, but we must NOT lose newHead
        dummy = newHead

        while dummy and dummy.next:
            if dummy.next.val < dummy.val: #next is smaller than current, means right side is larger, then we skip the next
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        
        prev = None
        curr = newHead

        while curr :
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev