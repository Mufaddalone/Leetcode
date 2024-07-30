# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node, a):
            if not node:
                return
            a.append(node.val)
            if not node.left and not node.right:  # Check for leaf node
                res.append(a[:])  # Store a copy of the current path
            else:
                if node.left:
                    dfs(node.left, a[:])  # Pass a copy to the left
                if node.right:
                    dfs(node.right, a[:])  # Pass a copy to the right

        dfs(root, [])
        print(res)  # This will show the paths as lists of values
        
        # Calculate the sum of numbers formed by the paths
        total_sum = 0
        for path in res:
            number = int(''.join(map(str, path)))
            total_sum += number
            
        return total_sum

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


        