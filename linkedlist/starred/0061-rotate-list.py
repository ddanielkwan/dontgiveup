# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0 :
            return head

        #get the length first
        #may be helpful


        length = 1
        tail = head #we need to move the tail

        while tail.next:
            length += 1
            tail = tail.next
        print(length)

        k = k % length

        if k == 0:
            return head
        
        curr = head
        #lets get the new head
        for _ in range(length - k - 1):
            curr = curr.next

        newHead = curr.next
        # 1 -> 2 -> 3-> 4->5
                # ^curr ^newhead
        curr.next = None  #cut the 3 -> 4 so now is 1 -> 2 -> 3 -> None

        print(newHead.val)

        #connect them
        tail.next = head
        return newHead


        



