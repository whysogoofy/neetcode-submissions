class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = self.right = None
    
    def print_node(self, node):
        temp = node
        st= ""
        while temp:
            st +=  "(" + str(temp.key) + ", " + str(temp.val) + ")"
            temp = temp.next
        print(st)

    def get(self, key: int) -> int:
        # print("get: ", key)
        node = self.cache.get(key, None)
        
        if not node:
            return -1
        elif node == self.right:
            return node.val

        node_prev = node.prev
        node_next = node.next
        if node_prev:
            node_prev.next = node_next
            node_next.prev = node_prev
        else:
            self.left = node_next
            node_next.prev = None

        node.prev = self.right
        node.next = None
        self.right.next = node
        self.right = node

        # self.print_node(self.left)
        # self.print_node(self.right)
        return node.val



    def put(self, key: int, value: int) -> None:
        # print("put: ", key, value)
        node = self.cache.get(key, None)

        if node:
            node.val = value
            self.get(key)
            return

        node = Node(key, value)
        self.cache[key] = node

        if not self.left and not self.right:
            self.left = self.right = node
            return 
        
        right = self.right
        right.next = node
        node.prev = right
        self.right = node

        if len(self.cache) > self.capacity:
            lru_key = self.left.key
            
            self.left = self.left.next
            self.left.prev = None
            # print("enter", lru_key, "put", key, value)
            self.cache.pop(lru_key, None)

        # print(len(self.cache))
        

        # self.print_node(self.left)
        # self.print_node(self.right)
        
        

        
