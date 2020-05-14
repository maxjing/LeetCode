"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        s = sorted([i for s in schedule for i in s], key=lambda x: x.start)
        res, end = [], s[0].end
        for i in s[1:]:
            if i.start > end:
                #2020.05.14 remember to put it into Interval
                res.append(Interval(end, i.start))
            end = max(end, i.end)
        return res
