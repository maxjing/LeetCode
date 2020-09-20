class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        num = []
        neg = False
        if x < 0:
            neg = True
        x = abs(x)
        while x > 0:
            num.append(x % 10)
            x = x // 10
        i = 0
        while i < len(num) and num[i] == 0:
            i += 1
        num = num[i:]
        res = int(''.join([str(x) for x in num]))
        if res > 2 ** 31 - 1:
            res = 0
        if neg:
            return (-res)
        return res


