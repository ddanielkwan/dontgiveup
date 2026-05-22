# Given the head of a singly linked list, group all the nodes with odd indices together followed by
#  the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd_dummy = ListNode(0)
        even_dummy = ListNode(0)

        odd = odd_dummy
        even = even_dummy

        curr = head
        index = 1

        while curr:
            if index % 2 == 1:  # odd index
                odd.next = curr
                odd = odd.next
            else:               # even index
                even.next = curr
                even = even.next
            curr = curr.next
            index += 1

        even.next = None        # terminate even list
        odd.next = even_dummy.next  # connect odd list to even list
        return odd_dummy.next

