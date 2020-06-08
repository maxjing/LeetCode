class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        prev_end = intervals[0][1]
        res = 0
        for interval in intervals[1:]:
            start, end = interval
            if start < prev_end:
                res += 1
            else:
                prev_end = end
        return res
'''
greedy, always choose the smallest end time 
thinking about the 1-100 if sort by start time, the rest will be removed 
'''