# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        res = []
        while q:
            a = []
            prev_val = None if len(res) % 2 == 0 else float('inf')
            for i in range(len(q)):
                node = q.popleft()
                # a.append(node.val)
                if len(res)%2 ==0:
                    if node.val%2 ==0 or (prev_val is not None and node.val <= prev_val):
                        return False
                else:
                    if node.val%2!=0 or (prev_val is not None and node.val >= prev_val):
                        return False
                prev_val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(a)
        return True

                