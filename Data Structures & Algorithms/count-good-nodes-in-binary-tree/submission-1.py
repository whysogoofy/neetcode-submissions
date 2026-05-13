# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, last_max):
            if not root:
                return 0

            dfs_left = dfs(root.left, max(last_max, root.val))
            dfs_right = dfs(root.right, max(last_max, root.val))

            count = dfs_left + dfs_right
            if root.val >= last_max:
                count += 1
            return count

        return dfs(root, root.val)