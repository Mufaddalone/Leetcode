# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,a):
            if not node: return
            if not node.left and not node.right:
                a.append(node.val)
            dfs(node.left,a)
            dfs(node.right,a)
            return a
        return (dfs(root1,[]) == dfs(root2,[]))
            