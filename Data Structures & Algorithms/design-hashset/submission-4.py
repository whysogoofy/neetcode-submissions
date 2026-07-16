class Node:
    def __init__(self, val=-1, next_node=None):
        self.val = val
        self.next_node = next_node

class MyHashSet:

    def __init__(self):
        self.arr = [None for _ in range(1000)]

    def add(self, key: int) -> None:
        index = key % 1000
        new_node = Node(key)
        
        if not self.arr[index]:
            self.arr[index] = new_node
            return
        
        curr = self.arr[index]

        if not curr.next_node and curr.val == key:
            return

        while curr.next_node:
            if curr.val == key:
                return
            curr = curr.next_node
        
        curr.next_node = new_node

    def remove(self, key: int) -> None:
        index = key % 1000
        curr = self.arr[index]

        if curr and curr.val == key:
            self.arr[index] = curr.next_node
            return

        while curr and curr.next_node:
            if curr.next_node and curr.next_node.val == key:
                curr.next_node = curr.next_node.next_node
                break

            curr = curr.next_node


    def contains(self, key: int) -> bool:
        index = key % 1000
        curr = self.arr[index]
        
        if not curr:
            return False
        
        while curr:
            if curr.val == key:
                return True

            curr = curr.next_node
        
        return False

        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)