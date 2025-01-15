# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1,t2 = headA,headB
        if not t1 or not t2:
                return None
        while t1!=t2:
            t1 = t1.next
            t2 = t2.next
            if t1 ==t2:return t1
            if t1== None:
                t1 = headB
            if t2 == None:
                t2 = headA
        return t1
        # z = set()
        # while headA:
        #     z.add(headA)
        #     headA = headA.next
        # while headB:
        #     if headB in z:
        #         return headB
        #     headB = headB.next
        # return None