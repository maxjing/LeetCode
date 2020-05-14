# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        half = self.reverse(slow)
        while half and head:
            if half.val != head.val:
                return False
            #2020.05.13 forgot to add.next
            half = half.next
            head = head.next
        return True

    def reverse(self, node):
        prev = None
        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev
