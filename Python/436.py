class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        maxStartHeap, maxEndHeap = [], []
        result = [0 for x in range(n)]
        for endIndex in range(n):
            heappush(maxStartHeap, (-intervals[endIndex][0], endIndex))
            heappush(maxEndHeap, (-intervals[endIndex][1], endIndex))
        for _ in range(n):
            topEnd, endIndex = heappop(maxEndHeap)
            if -maxStartHeap[0][0] >= -topEnd:
                # find the the interval that has the closest 'start'
                # 2020.05.16 [1, 2] -> [2, 3] (2 <= 2) so here use >=
                while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                    topStart, startIndex = heappop(maxStartHeap)
                result[endIndex] = startIndex
                # put the interval back as it could be the next interval of other intervals
                heappush(maxStartHeap, (topStart, startIndex))
            else:
                result[endIndex] = -1
        return result
