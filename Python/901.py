class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
'''
[100, 80, 60, 70, 60, 75, 85], stack = []
1. 100, stack = [[100, 1]] -> 1
2. 80, stack = [[100, 1], [80, 1]] -> 1
3. 60, [[100, 1], [80, 1], [60, 1]] -> 1
4. 70, [[100, 1], [80, 1], [70, 2]] (60 <= 70, res = 1 + 1, 60 poped) -> 2
5. 60 [[100, 1], [80, 1], [70, 2], [60, 1]] -> 1
6....

'''