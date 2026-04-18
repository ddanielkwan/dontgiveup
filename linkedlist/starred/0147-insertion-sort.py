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
        #so from this looks like we keep track 2
        # dummy -> head -> head.next
        #.         prev -> curr
        prev = head
        curr = head.next

        #check every node until end

        while curr:
            #maybe its already in order happy case
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
                continue
            
            #if not in order, we should start from beginning to see where to insert
            beginning = dummy

            #tells us where to insert our current node into #recall beginning is dummy to hel pus iterate
            while curr.val > beginning.next.val:
                beginning = beginning.next
            
            #perform swap for curr node and the pointer on where to insert
            #because  dummy -> 1 -> 4 -> 2 -> 3
            #                        ^prev ^ curr
            # we need to remove prev.next to be none or curr.next
            #so dummy -> 1 -> 4 -> 2 -> None
            #            ^ beginning
            # then dummy -> 1 ->3 -> 4 -> 2 ->
            prev.next = curr.next #move the curr node's previous to current node's next
            curr.next = beginning.next #since beginning is the last node that is less than curr.val
            beginning.next = curr
            curr = prev #reset to prev end that was sorted
              # then dummy -> 1 ->3 -> 4 -> 2 ->
                                    #    ^ prev
        
        return dummy.next