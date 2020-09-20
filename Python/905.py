class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        size = len(A)
        res = [0] * size
        l, r = 0, size - 1
        for n in A:
            if n % 2 == 0:
                res[l] = n
                l += 1
            else:
                res[r] = n
                r -= 1
        return res
