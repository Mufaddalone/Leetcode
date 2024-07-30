# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        def inorder(node):
            nonlocal prev
            if not node:
                return True
            if not (inorder(node.left) and prev < node.val):
                return False
            prev = node.val
            return inorder(node.right)
        return inorder(root)

        # if not root:
        #     return True
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node == None: return True
        #         if node.left and node.right:
        #             if node.left.val>=node.val or node.right.val<=node.val:
        #                 return False
        #         elif node.left:
        #             if node.left.val>=node.val:
        #                 return False
        #         elif node.right:
        #             if node.right.val<=node.val:
        #                 return False
        #         else:
        #             q.append(node.left)
        #             q.append(node.right)
        # return True

        
        