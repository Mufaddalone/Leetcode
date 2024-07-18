# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = [0]
        def dfs(node):
            if not node:
                return 
            if low<=node.val<=high:
                res[0] += node.val
            dfs(node.left)
            dfs(node.right)
            return res[0]
        return dfs(root)