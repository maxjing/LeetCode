# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(-1)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            if count == k:
                prev, current = r, l
                for _ in range(k):
                    next = current.next
                    current.next = prev
                    prev = current
                    current = next
                jump.next = prev
                jump = l
                l = r
            else:
                return dummy.next
