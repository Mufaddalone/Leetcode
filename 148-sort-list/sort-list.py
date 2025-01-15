# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mid(head):
            slow =head
            fast =head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(list1,list2):
            dummyNode = ListNode(-1)
            temp = dummyNode
            while list1  and list2 :
                if list1.val <= list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next
                temp = temp.next 
            if list1 is not None:
                temp.next = list1
            else:
                temp.next = list2
            return dummyNode.next
        def mergesort(head):
            if head is None or head.next is None:
                return head
            middle = mid(head)
            lefthead, righthead = head,middle.next
            middle.next = None
            ls = mergesort(lefthead)
            rs = mergesort(righthead)
            return merge(ls,rs)
        return mergesort(head)

