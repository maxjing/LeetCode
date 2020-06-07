class Solution:
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                res += sign * num
                sign = 1
                num = 0
            elif c == '-':
                res += sign * num
                sign = -1
                num = 0
            elif c == '(':
                # store the res and set res and sign to default
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                prev_sign = stack.pop()
                prev_res = stack.pop()
                res += sign * num
                # sign
                res *= prev_sign
                # prev value
                res += prev_res
                num = 0
        #2020.05.18 return outside for loop
        return res + num * sign


'''
initial: s = 1+(3-2), res = 0, sign = 1, num = 0
1. c = 1, num = 1, sign = 1, res = 0, stack = []
2. c = +, res = 1, sign = 1, num = 0, stack = []
3. c = (, stack = [1, 1], res = 0, sign = 1, num = 0
4. c = 3, num = 3, sign = 1, res = 0, stack = [1,1]
5. c = -, res = 3, sign = -1, num = 0, stack = [1, 1]
6. c = 2, num = 2, res += sign * num = 3 - 2 = 1, num = 0, stack = [1,1]
7. c = ), res += num * stack.pop() = 2 * 1 = 2, res *= stack.pop() = res * 1 = 2
'''
