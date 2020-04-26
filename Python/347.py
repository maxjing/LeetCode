# O(nlogk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        minHeap = []
        for key, value in d.items():
            heappush(minHeap, (value, key))
            if len(minHeap) > k:
                heappop(minHeap)
        res = []
        for _ in range(k):
            res.append(heappop(minHeap)[1])
        return res

# O(nlogn)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        res = []
        for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True):
            if k > 0:
                res.append(key)
            k -= 1
        return res
