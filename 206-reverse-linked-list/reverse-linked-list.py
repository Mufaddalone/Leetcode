# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr , prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev
        return head

"""
prev = None, 
cur = 1,
after = 2
1.next = None
prev = 1
cur = 2

after = 3
2.next = 1
prev = 2
cur = 3
"""  


        