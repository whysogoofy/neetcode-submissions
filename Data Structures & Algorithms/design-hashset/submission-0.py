class MyHashSet:

    def __init__(self):
        self.arr = [0 for _ in range(1000000)]

    def add(self, key: int) -> None:
        self.arr[key] = 1

    def remove(self, key: int) -> None:
        self.arr[key] = 0

    def contains(self, key: int) -> bool:
        return not not self.arr[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)