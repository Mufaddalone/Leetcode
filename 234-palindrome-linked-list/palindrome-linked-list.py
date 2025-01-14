# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        def reverse(head):
            curr = head
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        new_head = reverse(slow.next)
        first = head
        while new_head:
            if first.val!= new_head.val:
                return False
            new_head = new_head.next
            first = first.next
        return True
        # nums = []
        # while head:
        #     nums.append(head.val)
        #     head = head.next
        # l,r = 0 , len(nums)-1
        # while l<r:
        #     if nums[l]!=nums[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True

        