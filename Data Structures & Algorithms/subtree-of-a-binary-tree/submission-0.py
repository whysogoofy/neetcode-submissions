# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        def isTreeSame(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            
            return isTreeSame(p.left, q.left) and isTreeSame(p.right, q.right)
        
        stack = [root]

        while stack:
            node = stack.pop()
            if isTreeSame(node, subRoot):
                return True
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return False
        
        