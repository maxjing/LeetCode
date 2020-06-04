class Solution:
    def sumZero(self, n: int) -> List[int]:
        res, rem = [], n % 2
        if rem != 0:
            res.append(0)
        n //= 2
        for i in range(1, n+1):
            res.append(i)
            res.append(-i)
        return res