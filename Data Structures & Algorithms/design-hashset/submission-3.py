class Node:
    def __init__(self, val=-1, next_node=None):
        self.val = val
        self.next_node = next_node

class MyHashSet:

    def __init__(self):
        self.arr = [None for _ in range(10)]

    def add(self, key: int) -> None:
        index = key % 10
        # print("add", index)
        new_node = Node(key)
        
        if not self.arr[index]:
            self.arr[index] = new_node
            # if self.arr[index]:
            #     print("none case", self.arr[index].val)
            return
        
        curr = self.arr[index]

        if not curr.next_node and curr.val == key:
            return

        while curr.next_node:
            # print("while add", curr.val)
            if curr.val == key:
                # print("duplicate")
                return
            curr = curr.next_node
        
        curr.next_node = new_node
        # if self.arr[index]:
        #     print(self.arr[index].val)

    def remove(self, key: int) -> None:
        index = key % 10
        curr = self.arr[index]

        if curr and curr.val == key:
            self.arr[index] = curr.next_node
            return

        while curr and curr.next_node:
            if curr.next_node and curr.next_node.val == key:
                curr.next_node = curr.next_node.next_node
                break

            curr = curr.next_node
        
        # print("remove 2", self.arr[index])


    def contains(self, key: int) -> bool:
        index = key % 10
        # print("contains", index)
        curr = self.arr[index]
        
        if not curr:
            # print("first false", curr)
            return False
        # print("curr", curr.val)
        while curr:
            # print("while")
            if curr.val == key:
                return True

            curr = curr.next_node
        
        return False

        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)