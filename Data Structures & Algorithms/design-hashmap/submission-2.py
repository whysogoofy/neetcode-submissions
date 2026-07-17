class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.capacity = 1000
        self.arr = [None for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        index = key % self.capacity
        dummy = Node(-1, -1, self.arr[index])
        prev, curr = dummy, dummy.next

        while curr:
            if curr.key == key:
                curr.val = value
                return
            curr = curr.next
            prev = prev.next
        
        prev.next = Node(key, value)
        self.arr[index] = dummy.next
        

    def get(self, key: int) -> int:
        index = key % self.capacity
        curr = self.arr[index]

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> None:
        index = key % self.capacity
        dummy = Node(-1, -1, self.arr[index])
        prev, curr = dummy, dummy.next

        while curr:
            if curr.key == key:
                prev.next = curr.next
                break
            curr = curr.next
            prev = prev.next

        self.arr[index] = dummy.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)