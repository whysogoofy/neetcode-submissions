# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        output = dummy

        while l1 or l2:
            sum1 = l1.val if l1 else 0
            sum2 = l2.val if l2 else 0
            dummy.next = ListNode((sum1+sum2+carry) % 10)
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            carry = (sum1+sum2+carry) // 10
            dummy = dummy.next
        
        if carry:
            dummy.next = ListNode(carry)

        return output.next