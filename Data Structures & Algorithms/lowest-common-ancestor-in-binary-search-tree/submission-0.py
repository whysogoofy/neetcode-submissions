# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.output = None
        
        def dfs(root, p, q):
            if not root:
                return [False, False]

            dfs_left = dfs(root.left, p, q)
            dfs_right = dfs(root.right, p, q)

            isP = root.val == p.val or dfs_left[0] or dfs_right[0]
            isQ = root.val == q.val or dfs_left[1] or dfs_right[1]

            if isP and isQ and not self.output:
                self.output = root

            return [isP, isQ]
        
        dfs_root = dfs(root, p, q)

        return self.output

        