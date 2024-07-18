# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, target):
            if not node:
                return False
            if not node.left and not node.right:
                return target == node.val
            return (dfs(node.left, target - node.val) or dfs(node.right, target - node.val))
        
        return dfs(root, targetSum)
        # if not root:
        #     return False
        # def dfs(node,target):
        #     if target == 0:
        #         return True
        #     if not node:
        #         return
        #     left = dfs(node.left,target-node.val)
        #     right = dfs(node.right,target-node.val)
        #     return root
        # lf = dfs(root.left,targetSum)
        # rh = dfs(root.right,targetSum)
        # return lf or rh

        # def dfs(node,target):
        #     if target ==0:
        #         return True
        #     dfs(node.left,target-node.val)
        #     dfs(node.right,target-node.val)
        #     return root
        # return dfs(root,targetSum)
