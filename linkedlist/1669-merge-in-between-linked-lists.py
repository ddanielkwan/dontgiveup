# You are given two linked lists: list1 and list2 of sizes n and m respectively.

# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

# The blue edges and nodes in the following figure indicate the result:


# Build the result list and return its head.

 

# Example 1:


# Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [10,1,13,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode: # type: ignore
        
        #inclusive range [a,b] to remove
        #to get where the pointers start we need to loop a times to find
        curr = list1

        for _ in range(a-1):#a = 2 ->0,1, a-1 because we need the pointer to next         , this is the node before a
            print(curr.val)
            curr = curr.next
        
        aNode = curr #this is the node before a
        print(aNode.val)
        for _ in range(b-a+1):# + 1 because this is the final node we need t o remove
            curr = curr.next
        
        bNode = curr #this is the last node we need to remove
        print(bNode)

        aNode.next = list2 #set the node before the removed nodes, next's to list2
        curr = list2 #list2 is a head

        while curr: #go to the end of list2 and then set bNode to the next after end
            prev = curr
            curr = curr.next
        
        prev.next = bNode.next #because prev is the last node of list2 and bNode is the node we remove, so we use bnode.next
        return list1


