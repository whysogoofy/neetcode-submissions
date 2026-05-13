"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}

        curr = head

        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next

        curr = head
        dummy = Node(0, hashmap[curr] if curr else None, None)
        tail = dummy.next

        while curr:
            tail.next = hashmap[curr.next] if curr.next else None
            tail.random = hashmap[curr.random] if curr.random else None
            tail = tail.next
            curr = curr.next
        
        return dummy.next

            

