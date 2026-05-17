# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val          # value stored in the node
#         self.next = next        # pointer to the next node


#sortList:
    # if small → return “if small” means the base case — the smallest input size where no work is needed.
    # split list
    # sort left
    # sort right
    # merge
from typing import Optional

from linkedlist.ListNode import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We use merge sort because:
        # - Linked lists are good for splitting/merging
        # - Time complexity is O(n log n)
        # - No extra array space needed

        # Base case:
        # If the list is empty or has only one node, it is already sorted
        if not head or not head.next:
            return head
        
        # 'left' will point to the start of the left half
        left = head
        
        # Find the node *before* the midpoint
        mid = self.getMid(head)
        
        # 'right' starts at the node after mid
        right = mid.next

        # Cut the list into two halves
        # left half: head -> mid
        # right half: mid.next -> end
        mid.next = None
        
        # Recursively sort the left half
        left = self.sortList(left)
        
        # Recursively sort the right half
        right = self.sortList(right)

        # Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        # Merge two sorted linked lists (classic merge step of merge sort)

        # Dummy node to simplify edge cases
        tail = ListNode()
        dummy = tail

        # Compare nodes from both lists and attach the smaller one
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1      # attach l1
                l1 = l1.next         # move l1 forward
            else:
                dummy.next = l2      # attach l2
                l2 = l2.next         # move l2 forward
            
            dummy = dummy.next       # move merge pointer forward
        
        # Attach any remaining nodes (only one of these will run)
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        
        # Return the head of the merged list
        return tail.next

    def getMid(self, node):
        # This function returns the node *before* the midpoint
        # We do this so we can split the list cleanly

        slow = node      # moves one step at a time
        fast = node      # moves two steps at a time
        prev = None      # tracks node before slow

        # When fast reaches the end, slow is at the midpoint
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        # 'prev' is the node before the midpoint
        return prev

