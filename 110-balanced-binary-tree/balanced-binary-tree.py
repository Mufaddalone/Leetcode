# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:    
        return self.height(root) >= 0
    def height(self, root):
        if root is None:
            return 0
        l, r = self.height(root.left), self.height(root.right)
        if l == -1 or r== -1 or abs(l-r) > 1:
            return -1
        return 1 + max(l, r)
        # lens = [0]
        # if not root:
        #     return True
        # def dfs(node,lens):
        #     if not node:
        #         return 0
            
        #     left = dfs(node.left,lens)
        #     right= dfs(node.right,lens)

        #     lens = max(left,right)
        #     return max(left,right)+1
        # lef = dfs(root.left,lens)
        # rig = dfs(root.right,lens)
        # if abs(lef-rig) <=1:
        #     return True
        # else:
        #     return False