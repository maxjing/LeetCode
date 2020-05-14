# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        second_half = self.reverse(slow)
        first_half = head
        while first_half and second_half:
            temp = first_half.next
            first_half.next = second_half
            first_half = temp

            temp = second_half.next
            second_half.next = first_half
            second_half = temp
        # set the next of the last node to 'None'
        #2020.05.14 notice here
        if first_half is not None:
            first_half.next = None

    def reverse(self, node):
        prev = None
        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev
