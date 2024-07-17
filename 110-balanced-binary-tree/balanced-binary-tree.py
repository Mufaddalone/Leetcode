# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:   
        res = [True]
        def dfs(root):
            if not root:
                return res[0]
            lh = dfs(root.left)
            rh = dfs(root.right)
            if abs(lh - rh) > 1:
                res[0] = False
            return 1 + max(lh, rh)
        dfs(root)
        return res[0]
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