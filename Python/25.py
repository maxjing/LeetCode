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
            # 2020.05.14 it is else not out loop return
            else:
                return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev:
            prev = self.reverseNextKNodes(prev, k)
        return dummy.next

    def reverseNextKNodes(self, head, k):
        curr = head
        n1 = head.next
        for i in range(k):
            curr = curr.next
            if not curr:
                return None
        nk = curr
        nkplus = curr.next

        prev = head
        curr = head.next

        while curr != nkplus:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        head.next = nk
        n1.next = nkplus
        return n1
