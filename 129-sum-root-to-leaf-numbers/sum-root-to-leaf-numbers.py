# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,num):
            if not node:return 0
            num = num*10 + node.val
            if not node.left and not node.right:
                return num
            return (dfs(node.left,num)+dfs(node.right,num))
        return dfs(root,0)


        # res= []
        # def dfs(node,a):
        #     if not node.left and not node.right:
        #         a.append(node.val)
        #         res.append(a)
        #         return
        #     a.append(node.val)
        #     dfs(node.left,a)
        #     dfs(node.right,a)
        # dfs(root,[])
        # print(res)
        # return sum(res)


        