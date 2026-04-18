# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #so we want to have at least two nodes to swap

        dummy = ListNode(0, head)

        prev = dummy
        curr = head
        #while there is two elements,
        # Dummy -> curr -> curr.next -> curr.next.next
        # prev ^ prev.next^    second^      
        while curr and curr.next:
            #note: curr will act as the first node 
            #and curr.next will act as the second node

            nxtPair = curr.next.next #next node after second
            second = curr.next #as we said before

            #reverse
            prev.next = second
            second.next = curr
            curr.next = nxtPair

            #update ptrs
            prev = curr
            curr = nxtPair
        
        return dummy.next