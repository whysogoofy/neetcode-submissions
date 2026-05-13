# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth, stack = 1, [[root, 1]]
        
        while stack:
            d = stack.pop()
            max_depth = max(max_depth, d[1])
            
            if d[0].right:
                stack.append([d[0].right, d[1] + 1])
            if d[0].left:
                stack.append([d[0].left, d[1] + 1])
        
        return max_depth
