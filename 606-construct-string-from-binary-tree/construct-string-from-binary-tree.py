# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        def preorder(root: Optional[TreeNode]) -> str:
            if not root:
                return ""
            left = preorder(root.left)
            right = preorder(root.right)

            if not root.left and not root.right:
                return f"{root.val}"
            if not root.right:
                return f"{root.val}({left})"
                
            return f"{root.val}({left})({right})"
        
        return preorder(root)

            