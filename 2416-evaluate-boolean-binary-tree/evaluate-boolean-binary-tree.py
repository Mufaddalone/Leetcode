# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.right and not root.left:
            return False if root.val == 0 else True
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
                
        return self.evaluateTree(root.right) and self.evaluateTree(root.left)
            