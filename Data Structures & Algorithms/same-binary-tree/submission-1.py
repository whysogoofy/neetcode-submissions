# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p, stack_q = [p] if p else [], [q] if q else []

        while stack_p:
            node_p = stack_p.pop()
            # print(node_p.val)
            if not stack_q:
                # print("here")
                return False
            node_q = stack_q.pop()

            if node_p.val != node_q.val or (node_p.left and not node_q.left) or (node_p.right and not node_q.right):
                return False
            # if node_p.val != node_q.val:
            #     return False
            
            if node_p.right:
                stack_p.append(node_p.right)
            if node_p.left:
                stack_p.append(node_p.left)
            if node_q.right:
                stack_q.append(node_q.right)
            if node_q.left:
                stack_q.append(node_q.left)
        
        if stack_q:
            return False

        return True
            
            
