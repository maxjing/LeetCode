class Solution:
    maxHeap, minHeap = [], []

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = [0.0 for x in range(len(nums) - k + 1)]
        for i in range(0, len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])

            self.rebalance()
            # reach window limit
            if i - k + 1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    result[i - k + 1] = -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
                else:
                    result[i - k + 1] = -self.maxHeap[0] / 1.0
                elementToRemove = nums[i - k + 1]
                # 2020.05.16 notice the negative sign
                if elementToRemove <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -elementToRemove)
                else:
                    self.remove(self.minHeap, elementToRemove)
                self.rebalance()
        return result

    def remove(self, heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]
        # O(logn)
        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)

    def rebalance(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))


'''
Time complexity #

The time complexity of our algorithm is O(N*K) where ‘N’ is the total number of elements in the input array and ‘K’ is the size of the sliding window. This is due to the fact that we are going through all the ‘N’ numbers and, while doing so, we are doing two things:

    1. Inserting/removing numbers from heaps of size ‘K’. This will take O(logK)
    2. Removing the element going out of the sliding window. This will take O(K) as we will be searching this element in an array of size ‘K’ (i.e., a heap).

'''
