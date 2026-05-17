# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool: # type: ignore
        
        #palindrome means in middle is equals left and right
        #lets reverse the right portion and iterate to determine whethjer elements are equal

        #step1 get the middle
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #slow is where the mid is 
        #reverse it now
        curr = slow
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        #the second portion reversed head is now at prev
        front = head

        while front and prev:
            if front.val != prev.val:
                return False
            
            front = front.next
            prev = prev.next
        
        return True
        

