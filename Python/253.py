class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        start = []
        end = []
        res = 0
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])

        start.sort()
        end.sort()

        enditr = 0
        for i in range(len(start)):
            if start[i] < end[enditr]:
                res += 1
            else:
                enditr += 1
        return res
