class LRUCache:

    def __init__(self, capacity: int):
        self.q = deque()
        self.d = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.q.remove(key)
        self.q.append(key)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.q.remove(key)
        elif len(self.d) == self.capacity:
            del self.d[self.q.popleft()]
        self.q.append(key)
        self.d[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
