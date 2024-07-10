# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node,res):
            # Base case: if the node is None, return 0
            if not node:
                return 0
            
            # Recursively calculate the diameter of left and right subtrees
            left = dfs(node.left, res)
            right = dfs(node.right, res)

            # Update the maximum diameter encountered so far
            res[0] = max(res[0], left + right)
            
            # Return the depth of the current node
            return max(left, right) + 1
        
        # Initialize a list to hold the maximum diameter encountered
        res = [0]
        # Call the diameter function starting from the root
        dfs(root, res)
        # Return the maximum diameter encountered
        return res[0]

