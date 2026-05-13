# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr, ret = l1, l1

        while l1 or l2:
            sum1 = l1.val if l1 else 0
            sum2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr.next = ListNode((sum1+sum2+carry)%10)
            curr = curr.next
            carry = (sum1+sum2+carry) // 10
        
        if carry:
            curr.next = ListNode(carry)

        return ret.next