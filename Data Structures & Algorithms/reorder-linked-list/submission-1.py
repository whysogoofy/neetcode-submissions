# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next
        
        max_len = len(stack)
        tail = head

        for _ in range((max_len) // 2):
            next_tail = tail.next
            node = stack.pop()
            
            node.next = next_tail
            tail.next = node

            tail = next_tail 

        tail.next = None
