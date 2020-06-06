#TLE
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        minHeap, res, visited = [], [-1] * len(workers), set()
        for i in range(len(bikes)):
            for j in range(len(workers)):
                heappush(minHeap, (self.distance(workers[j], bikes[i]), j, i))
        count = 0
        while minHeap and count < len(res):
            _, worker_idx, bike_idx = heappop(minHeap)
            if bike_idx not in visited and res[worker_idx] == -1:
                count += 1
                visited.add(bike_idx)
                res[worker_idx] = bike_idx
        return res

    def distance(self, worker, bike):
        x1, y1 = worker
        x2, y2 = bike
        return abs(x1 - x2) + abs(y1 - y2)
