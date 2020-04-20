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
        # if start time is smaller than last end time, means there is a meeting before the current meeting and has not finished yet, so count + 1, else check the next room
        for i in range(len(start)):
            if start[i] < end[enditr]:
                res += 1
            else:
                enditr += 1
        return res
