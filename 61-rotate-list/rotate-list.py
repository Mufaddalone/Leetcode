# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findnew(temp,n):
            n-=1
            while n:
                n-=1
                temp = temp.next
            return temp
        if head == None or k==0:
            return head
        temp = head
        count =1
        while temp.next:
            count+=1
            temp=temp.next
        temp.next = head
        print(count)
        k = k%count
        print(k)
        newNode = findnew(head,count-k)
        head = newNode.next
        newNode.next = None
        return head

        