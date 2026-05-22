# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:


# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.


class Solution:
    #because both traveling same distance so always intersefct
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: # type: ignore
        

        listA = headA
        listB = headB   
        #so if you have a = 5 nodes nad b = 5 nodes, and at most it will go to 10 nodes sright intersects at null worse case

        # Continue until both pointers have traversed both lists
        while listA or listB:
            
            # If both pointers point to the same node,
            # we found the intersection
            if listA == listB:
                return listA
            
            # Move listA forward
            # If it reaches the end, jump to headB
            listA = listA.next if listA else headB
            
            # Move listB forward
            # If it reaches the end, jump to headA
            listB = listB.next if listB else headA
        

        return None

