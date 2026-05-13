# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy, stack = ListNode(0, head), []
        tail = dummy.next
        last_head = dummy

        while tail:
            # print("iterator", last_head.val, tail.val)
            stack.append(tail)
            tail = tail.next
            if len(stack) == k:
                while stack:
                    node = stack.pop()
                    if len(stack) == k - 1:
                        last_head.next = node
                    if len(stack) == 0:
                        last_head = node
                    node.next = stack[-1] if stack else tail
            
            # st = "("
            # for ele in stack:
            #     st += str(ele.val) + ","
            # print(st + ")")
        
        return dummy.next

                


                
                