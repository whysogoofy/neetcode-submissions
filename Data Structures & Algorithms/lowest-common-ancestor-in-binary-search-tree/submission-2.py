# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        max_val = max(p.val, q.val)
        min_val = min(p.val, q.val)

        while root:
            if root.val < min_val:
                root = root.right
            elif root.val > max_val:
                root = root.left
            else:
                return root

        
