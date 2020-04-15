# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        cycleLength = 0
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycleLength = self.getCycleLength(slow)
                break
        return self.findStart(head, cycleLength) if cycleLength != 0 else None

    def getCycleLength(self, node):
        temp = node
        l = 0
        while True:
            temp = temp.next
            l += 1
            if temp == node:
                break
        return l

    def findStart(self, head, length):
        p1, p2 = head, head
        while length > 0:
            p2 = p2.next
            length -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

# method 2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        try:
            slow = head.next
            fast = head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        isCycle = False
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                isCycle = True
                break
        if isCycle == False:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
