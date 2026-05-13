# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.arr = []

        def dfs(node):
            if not node:
                self.arr.append("null")
                return
            self.arr.append(str(node.val))
            
            dfs(node.left)
            dfs(node.right)

            return
        dfs(root)
        
        return ",".join(self.arr)
        



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        self.index = 0

        def dfs():
            if arr[self.index] == "null":
                self.index += 1
                return
            
            node = TreeNode(int(arr[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
        


