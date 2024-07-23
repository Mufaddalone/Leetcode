# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, level):
            if not node:
                return
            
            # If we reach a new level, add a new list to the result
            if len(res) == level:
                res.append([])
            
            # Append the current node's value to its corresponding level list
            res[level].append(node.val)
            
            # Recur for left and right children
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        
        res = []
        helper(root, 0)
        return res
        
        # if not root:
        #     return []
        # q = deque([root])
        # res = []
        # while q:
        #     val = []
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         val.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     res.append(val)
        # return res

        
        # if not root:
        #     return []
        # q = deque([root])
        # a = [[root.val]]

        # while q:
        #     b = []
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left and node.right:
        #             b.append(node.left.val)
        #             b.append(node.right.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #         elif node.left:
        #             b.append(node.left.val)
        #             q.append(node.left)
        #         elif node.right:
        #             b.append(node.right.val)
        #             q.append(node.right)
        #     a.append(b)
        # a.pop()
        # return a


            


        