# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, node: Optional[TreeNode]) -> bool:
        if not node.right and not node.left:
            return False if node.val == 0 else  True
        if node.val == 2:
            return self.evaluateTree(node.left) or self.evaluateTree(node.right)
        
        return self.evaluateTree(node.left) and self.evaluateTree(node.right)
            