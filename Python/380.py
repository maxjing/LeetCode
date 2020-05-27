class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = list()
        self.size = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.list:
            self.size += 1
            self.list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.list:
            self.list.remove(val)
            self.size -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        seed = random.randint(0, self.size - 1)
        return self.list[seed]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

'''
follow up optimize:
1 . use d, look up only take o(1), d store value and index
2. when remove switch removed one to last, and pop it
'''


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = list()
        self.d = {}
        self.idx = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        else:
            self.d[val] = self.idx
            self.idx += 1
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.d:
            idx = self.d[val]
            lastidx = len(self.list) - 1
            lastval = self.list[-1]

            self.list[idx], self.list[lastidx] = self.list[lastidx], self.list[idx]
            self.d[lastval] = idx
            self.list.pop()
            self.idx -= 1
            del self.d[val]
            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()