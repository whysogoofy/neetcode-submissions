# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, float("-infinity"), float("infinity")]

            dfs_left = dfs(root.left)
            dfs_right = dfs(root.right)
            left_bol = dfs_left[0]
            left_max = dfs_left[1]
            left_min = dfs_left[2]
            right_bol = dfs_right[0]
            right_max = dfs_right[1]
            right_min = dfs_right[2]
            
            bol = left_bol and right_bol and left_max < root.val and right_min > root.val

            return [bol, max(root.val, right_max, left_max), min(root.val, right_min, left_min) ]
        
        return dfs(root)[0]
        