# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        ## Parameter
        # node: tree node
        # occurrence: bit flag for number 1 ~ 9
        def check(node=None, occurrence=0):

            # Base case for empty tree
            if not node:
                return 0
            
            # Toggle bit flag for current node value
            occurrence ^= (1 << node.val)

            # Count pseudo palindromeic path in current tree
            palin_count = check(node.left, occurrence) + check(node.right, occurrence)
            if not node.left and not node.right:
                # Now, we are at leaf node, update pseudo palindromeic path count if at most one number has odd occurrence
                palin_count += ( (occurrence & occurrence-1) == 0 )

            return palin_count

        # ======================================
        return check(node=root, occurrence=0)
        