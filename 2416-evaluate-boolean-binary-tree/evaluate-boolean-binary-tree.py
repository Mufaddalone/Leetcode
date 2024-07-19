# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return False
            if node.val == 0:
                return False
            if node.val == 1:
                return True
            l = dfs(node.left)
            r = dfs(node.right)
            if node.val == 2:
                return l or r
            if node.val == 3:
                return l and r
            
        return dfs(root)
            