class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = []
        currentMax = -math.inf
        for list in nums:
            heappush(minHeap, (list[0], 0, list))
            currentMax = max(currentMax, list[0])
        rangeStart, rangeEnd = 0, math.inf
        while len(minHeap) == len(nums):
            num, i, list = heappop(minHeap)
            if rangeEnd - rangeStart > currentMax - num:
                rangeStart = num
                rangeEnd = currentMax
            if len(list) > i + 1:
                heappush(minHeap, (list[i + 1], i + 1, list))
                currentMax = max(currentMax, list[i + 1])
        return [rangeStart, rangeEnd]
