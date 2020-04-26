class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        maxHeap = []
        for i in range(K):
            heappush(maxHeap, (self.distance(points[i]), points[i]))
        for i in range(K, len(points)):
            if self.distance(points[i]) > maxHeap[0][0]:
                heappop(maxHeap)
                heappush(maxHeap, (self.distance(points[i]), points[i]))
        res = []
        for _ in range(K):
            res.append(heappop(maxHeap)[1])
        return res

    # maxheap so change to negative value, and ignoring sqrt
    def distance(self, point):
        return -point[0] * point[0] - point[1] * point[1]
