# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
    

        first = l1
        second = l2

        carry = 0 #because two numbers added and > 9 will have carry
        dummy = ListNode()  #this will be iterator
        iterator = dummy #pointer to beginning

        while l1 or l2 or carry: #if l1 or l2 exists or theres even a carry then make the addition
            f = l1.val if l1 else 0
            s = l2.val if l2 else 0

            digits = f + s + carry
            digit = digits % 10 #get single digit
            carry = digits // 10 #get carry, can only be 1 or none

            nxt = ListNode(val = digit)
            iterator.next = nxt
            iterator = iterator.next
        
        
            #if numbers are not same length
            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        return dummy.next