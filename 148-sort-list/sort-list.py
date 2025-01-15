# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        a = []
        while temp:
            a.append(temp.val)
            temp = temp.next
        a.sort()
        temp = head
        for i in range(len(a)):
            temp.val = a[i]
            temp = temp.next
        return head
