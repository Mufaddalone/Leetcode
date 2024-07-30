# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        preval = float('-inf')  # Start with the smallest possible value
        a = []
        
        def dfs(node, preval):
            if not node:
                return
            if node.val >= preval:
                a.append(node.val)
                preval = node.val  # Update preval to current node's value
            dfs(node.left, preval)
            dfs(node.right, preval)
        
        dfs(root, preval)
        return len(a)


