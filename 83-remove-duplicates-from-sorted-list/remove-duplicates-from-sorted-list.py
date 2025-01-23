# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            nxt = temp.next
            while nxt and nxt.val==temp.val:
                nxt = nxt.next
            temp.next = nxt
            temp=temp.next
        return head