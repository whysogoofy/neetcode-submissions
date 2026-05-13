# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        diameter = 0

        while stack:
            node = stack.pop()
            diameter = max(diameter, self.maxDepth(node.left) + self.maxDepth(node.right))

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return diameter
            

