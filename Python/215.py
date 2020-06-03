class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for i in range(k):
            heappush(minHeap, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > minHeap[0]:
                heappop(minHeap)
                heappush(minHeap, nums[i])
        return minHeap[0]


'''
Time: O(nlogk)
如果是需要全部放进去才能知道确定答案的话， largest 就用 minheap
#378 那种情况是sort着放的 smallest也用minheap， 不用全部放进去
'''
