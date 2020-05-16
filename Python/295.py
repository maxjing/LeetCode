class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    # o(logn)
    def addNum(self, num: int) -> None:
        # 2020.05.16 [] will never be none so use not
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
        else:
            return -self.maxHeap[0] / 1.0

# [3, 1, 5, 4]
# 1. maxHeap:[3]
# 2. maxHeap: [3, 1] -> need balance size -> maxHeap[1], minHeap[3]  -> median: 2
# 3. maxHeap[3], minHeap[1, 5] -> maxHeap[3, 1], minHeap[5] -> median: 3
# 4. maxHeap[3, 1], minHeap[4, 5] -> median: 3.5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
