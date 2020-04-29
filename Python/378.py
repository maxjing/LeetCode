class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        for list in matrix:
          # insert first element, and index
            heappush(minHeap, (list[0], 0, list))
        count, num = 0, 0
        while minHeap:
            num, i, list = heappop(minHeap)
            count += 1
            if count == k:
                break
            if len(list) > i + 1:
                heappush(minHeap, (list[i + 1], i + 1, list))
        return num


'''
Time: O(klogn)
'''
