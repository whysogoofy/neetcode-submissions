# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathforNode(self, node):
        if not node:
            return 0
        
        max_path_left = self.maxPathforNode(node.left)
        max_path_right = self.maxPathforNode(node.right)

        # print(node.val, max_path_left, max_path_right)
        self.max_path = max(self.max_path, max_path_left + max_path_right + node.val, node.val + max(max_path_left, max_path_right), node.val)
        # print("max_path", self.max_path)

        return max(node.val + max(max_path_left, max_path_right), node.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float("-infinity")
        
        self.maxPathforNode(root)
        # print(maxPathforNode(root))
    
        return self.max_path