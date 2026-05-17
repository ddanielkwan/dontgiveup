# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # type: ignore
        if not head:
            return

        curr = head
        for _ in range(n):
            curr = curr.next
        if not curr: #if 1>2>3 and n == 3 curr will be at null so the first elemnet has to die which means the Nth node from the end is the head itself
        #so we return head.next
            return head.next


        slow = head
        while curr and curr.next:
            curr = curr.next
            slow = slow.next
        
        slow.next = slow.next.next if slow.next else None
        return head

