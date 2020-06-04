class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(bin(n))
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        if '1' in d:
            return d['1']
        else:
            return 0

class Solution:
    def hammingWeight(self, n: int) -> int:
        #bin -> change to binary string
        res = bin(n).count('1')
        return res

class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c
'''
If n = 00101100, then n - 1 = 00101011, so n & (n - 1) = 00101100 & 00101011 = 00101000. Count = 1.
If n = 00101000, then n - 1 = 00100111, so n & (n - 1) = 00101000 & 00100111 = 00100000. Count = 2.
If n = 00100000, then n - 1 = 00011111, so n & (n - 1) = 00100000 & 00011111 = 00000000. Count = 3.
'''