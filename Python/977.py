class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                res.append(left * left)
                l += 1
            else:
                res.append(right * right)
                r -= 1
        return res[::-1]
