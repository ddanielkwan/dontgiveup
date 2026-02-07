# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# The steps of the insertion sort algorithm:

# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         #we use dummy to keep tracak make it easier to insert at beginnng
        dummy = ListNode(0, head)

        prev = head
        curr = head.next

        #check every node until end

        while curr:
            #maybe its already in order
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
                continue
            
            #if not in order, we should start from beginning to see where to insert
            beginning = dummy

            #tells us where to insert our current node into
            while curr.val > beginning.next.val:
                beginning = beginning.next
            
            #perform swap for curr node and the pointer on where to insert
            prev.next = curr.next #move the curr node's previous to current node's next
            curr.next = beginning.next #since beginning is the last node that is less than curr.val
            beginning.next = curr
            curr = prev
        
        return dummy.next