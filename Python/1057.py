class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                distances.append((self.distance(w, b), i, j))
        distances.sort()
        bike_taken = set()
        res = [-1] * len(workers)
        for _, worker_idx, bike_idx in distances:
            if len(bike_taken) == len(workers):
                break
            if res[worker_idx] == -1 and bike_idx not in bike_taken:
                res[worker_idx] = bike_idx
                bike_taken.add(bike_idx)
        # when bike is less than woker, return 0
        for i in range(len(res)):
            if res[i] == -1:
                res[i] = 0
        return res

    def distance(self, worker, bike):
        x1, y1 = worker
        x2, y2 = bike
        return abs(x1 - x2) + abs(y1 - y2)
'''
Instead use heap to heapfy everything, just use a array to store distance, i,j and sort it  
'''
#TLE
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        minHeap, res, visited = [], [-1] * len(workers), set()
        for i in range(len(bikes)):
            for j in range(len(workers)):
                heappush(minHeap, (self.distance(workers[j], bikes[i]), j, i))
        d = {}
        while len(d) < len(workers):
            _, worker_idx, bike_idx = heappop(minHeap)
            if worker_idx in d or bike_idx in visited:
                continue
            d[worker_idx] = bike_idx
            visited.add(bike_idx)
        for key, v in d.items():
            res[key] = v
        return res

    def distance(self, worker, bike):
        x1, y1 = worker
        x2, y2 = bike
        return abs(x1 - x2) + abs(y1 - y2)
