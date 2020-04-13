class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])
        newInterval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= newInterval[1]:
                newInterval[1] = max(newInterval[1], intervals[i][1])
                if i == 1:
                    res.append(newInterval)
            else:
                if i == 1:
                    res.append(newInterval)
                res.append(intervals[i])
                newInterval = intervals[i]
        return res


'''
Time: O(nlogn), logn for sort, n for loop
Space: O(n) s we need to return a list containing all the merged intervals. We will also need O(N) space for sorting
'''
