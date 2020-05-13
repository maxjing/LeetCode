class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = self.binarySearch(arr, x)
        l, r = index - k, index + k
        # l cannot be smaller than 0
        # r cannot be larger than size
        l = max(0, l)
        r = min(r, len(arr) - 1)
        minHeap = []
        for i in range(l, r + 1):
            heappush(minHeap, (abs(arr[i] - x), arr[i]))
        res = []
        for _ in range(k):
            res.append(heappop(minHeap)[1])
        res.sort()
        return res

    def binarySearch(self, arr, x):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                r = mid - 1
            else:
                l = mid + 1
        return l

#nlogn
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap = []
        arr.sort()
        for n in arr:
            heappush(maxHeap, (-abs(n - x), -n))
            if len(maxHeap) > k:
                heappop(maxHeap)
        res = []
        while maxHeap:
            res.append(-heappop(maxHeap)[1])
        res.sort()
        return res