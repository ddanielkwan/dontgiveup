
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None: # type: ignore
        """ 
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return

        #step one find the middle

        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        secondHalf = slow.next #remove the connection we remove the connection to prevent cycles and to clearly separate the two halves before reversing and merging
        slow.next = None

        reverse = secondHalf
        prev = None
        while reverse:
            tmp = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = tmp
        
        #head is now prev
        l1 = head
        l2 = prev

        while l2:
            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2
            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2



