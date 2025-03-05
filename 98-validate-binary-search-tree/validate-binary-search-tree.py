# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,left,right):
            if not node:return True
            if node.val<=left or node.val>=right:
                return False
            return (dfs(node.left,left,node.val) and dfs(node.right,node.val,right))
        return dfs(root,float("-inf"),float("inf"))
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