class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(K):
            return sum(math.ceil(pile / K) for pile in piles) <= H
        total = sum(piles)
        l, h = 1, max(piles)
        while l < h:
            m = l + (h - l) // 2
            if possible(m):
                h = m
            else:
                l = m + 1
        return l
