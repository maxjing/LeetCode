class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = Counter(arr)
        res = len(d)
        minHeap = []
        for key, value in d.items():
            heappush(minHeap, (value, key))
        while k > 0:
            value, key = heappop(minHeap)
            if value <= k:
                res -= 1
                k -= value
            else:
                break
        return res
                
    