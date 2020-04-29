class FreqStack:

    def __init__(self):
        self.d = {}
        self.maxHeap = []
      # use as sequence
        self.count = 0

    def push(self, x: int) -> None:
        self.count += 1
        self.d[x] = self.d.get(x, 0) + 1
        heappush(self.maxHeap, (-self.d[x], -self.count, x))

    def pop(self) -> int:
        freq, count, val = heappop(self.maxHeap)
        self.d[val] -= 1
        if self.d[val] == 0:
            del self.d[val]
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
