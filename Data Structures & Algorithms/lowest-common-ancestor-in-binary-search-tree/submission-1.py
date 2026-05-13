# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        max_val = max(p.val, q.val)
        min_val = min(p.val, q.val)

        while stack:
            node = stack.pop()

            if node.val == p.val or node.val == q.val or (node.val < max_val and node.val > min_val):
                return node
            elif node.val < min_val:
                stack.append(node.right)
            elif node.val > max_val:
                stack.append(node.left)

        
