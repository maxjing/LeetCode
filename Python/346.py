class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.q = deque()

    def next(self, val: int) -> float:
        q = self.q
        q.append(val)
        if len(q) > self.size:
            q.popleft()
        return sum(q) / len(q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)