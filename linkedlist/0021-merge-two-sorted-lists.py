# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        
        l1 = list1
        l2 = list2

        dummy = ListNode()
        ret = dummy

        while l1 and l2 :
            if l1.val < l2.val:
                ret.next = l1
                l1 = l1.next
            else:
                ret.next = l2
                l2 = l2.next
            ret = ret.next
        
        if l1:
            ret.next = l1
        if l2:
            ret.next = l2
        
        return dummy.next

