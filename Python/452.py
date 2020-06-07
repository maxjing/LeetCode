class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = sorted(points, key=lambda x: x[1])
        shoot = points[0][1]
        res = 1
        for start, end in points[1:]:
            # no need check end for sure less than
            if shoot < start:
                res += 1
                shoot = end
        return res
