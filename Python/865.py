class ExamRoom(object):

    def __init__(self, N):
        self.N, self.L = N, []

    def seat(self):
        N, L = self.N, self.L
        if not L:
            res = 0
        else:
            # 1. find distance from 0
            d, res = L[0], 0
            # 2. find in the middle
            for a, b in zip(L, L[1:]):
                if (b - a) // 2 > d:
                    d, res = (b - a) // 2, (b + a) // 2
            # 3. find from the end
            if N - 1 - L[-1] > d:
                res = N - 1
        bisect.insort(L, res)
        # L.append(res)
        # L.sort()
        return res

    def leave(self, p):
        self.L.remove(p)
