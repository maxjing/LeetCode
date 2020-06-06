class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = abs(C - A) * abs(D - B)
        area2 = abs(G - E) * abs(H - F)
        w = min(C, G) - max(A, E)
        h = min(D, H) - max(B, F)

        if w <= 0 or h <= 0:
            return area1 + area2
        else:
            return area1 + area2 - w * h
