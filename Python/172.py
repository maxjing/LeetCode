class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n // 5
            n //= 5
        return res
'''
有几个2*5就有几个0， 5的数量远远少于2
'''






