# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root])
        st = ""
        extra_level_tracker = 0

        while q:
            save_len = len(q)
            extra_level_tracker = 0
            for i in range(save_len):
                node = q.popleft()
                if node:
                    st += str(node.val) + ","
                    q.append(node.left)
                    q.append(node.right)
                else:
                    st +=  "null,"
                    extra_level_tracker += 1
        
        return str(extra_level_tracker) + "," + st[:len(st)-1]
        



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # print(data)
        curr = root = TreeNode()

        q = deque([curr])
        q_in = deque(data.split(","))

        extra_nodes = int(q_in.popleft())
        root_val = q_in.popleft()
        q_in = deque(list(q_in)[:len(list(q_in)) - extra_nodes])
        # print("new", q_in)

        if root_val == "null":
            root = None
        else:
            root.val = root_val

        while q_in:
            for i in range(len(q)):
                node = q.popleft()
                # print(node.val if node else None)
                # print(q_in)

                if node:
                    left_node_val = q_in.popleft() if q_in else None
                    right_node_val = q_in.popleft() if q_in else None
                    node.left = TreeNode(left_node_val) if left_node_val != "null" else None
                    node.right = TreeNode(right_node_val) if right_node_val != "null" else None
                    q.append(node.left)
                    q.append(node.right)

        
        return root
