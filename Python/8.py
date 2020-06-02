class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.lstrip()
        if not s:
            return 0
        num, sign = 0, 1
        if s[0] in '+-':
            sign = s[0] == '+'
            s = s[1:]
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                break

        num = num if sign else -num
        num = max(num, -2 ** 31)
        num = min(num, 2 ** 31 - 1)
        return num