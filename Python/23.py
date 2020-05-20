# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    ListNode.__eq__ = lambda self, other: self.val == other.val
    # less than
    ListNode.__lt__ = lambda self, other: self.val < other.val

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(-1)
        d = dummy
        minHeap = []
        for list in lists:
            #2020.05.18 forgot this again
            if list is not None:
                heappush(minHeap, list)
        while minHeap:
            node = heappop(minHeap)
            next = node.next
            node.next = None
            d.next = node
            d = d.next
            if next is not None:
                heappush(minHeap, next)
        return dummy.next
