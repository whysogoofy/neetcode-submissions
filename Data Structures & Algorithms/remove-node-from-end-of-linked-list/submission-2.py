# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        iterator, prev = head, None

        while iterator:
            temp = iterator.next
            iterator.next = prev
            prev = iterator
            iterator = temp
        # print(prev.val)
        second_it, prev_2, index = prev, None, 1

        if n == 1:
            second_it = second_it.next

        while second_it:
            # print(index)
            if index == n - 1:
                # print("enter", second_it.next.val)
                second_it.next = second_it.next.next
                # print("enter update", second_it.next.val)
            temp = second_it.next
            second_it.next = prev_2
            prev_2 = second_it
            second_it = temp
            # if n == 1 and index == 1:

            #     if second_it:
            #         second_it = second_it.next
            #     prev_2 = temp
            index += 1
        
        return prev_2

