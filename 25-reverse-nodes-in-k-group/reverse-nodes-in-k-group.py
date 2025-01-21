# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(temp):
            curr = temp
            prev =None
            while curr:
                nxt = curr.next
                curr.next= prev
                prev = curr
                curr = nxt
            return prev
        def kthgroup(temp,k):
            k-=1
            while temp and k>0:
                k-=1
                temp = temp.next
            return temp
        temp = head
        prevNode = None
        while temp:
            kthnode = kthgroup(temp,k)
            if kthnode == None:
                if prevNode:
                    prevNode.next = temp
                break
            nextNode = kthnode.next
            kthnode.next = None
            rev(temp)
            if temp == head:
                head = kthnode
            else:
                prevNode.next=kthnode
            prevNode = temp
            temp = nextNode
        return head

            

            


