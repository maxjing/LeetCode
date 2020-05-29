class Solution:
    def calculate(self, s: str) -> int:
        stack, num, prev_sign = [], 0, '+'
        s.replace(' ', '')
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            if c in '+-*/' or c == s[-1]:
                if prev_sign == '+':
                    stack.append(num)
                if prev_sign == '-':
                    stack.append(-num)
                if prev_sign == '*':
                    stack.append(stack.pop() * num)
                    # 2020.05.28 pay attention to /, case 10-2/3 without abs(pop) will give 9, prevent it do -2/3
                if prev_sign == '/':
                    p = stack.pop()
                    res = abs(p) // num
                    stack.append(res if p >= 0 else -res)

                prev_sign = c
                num = 0
        return sum(stack)
