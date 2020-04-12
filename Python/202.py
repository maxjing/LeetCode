class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = self.getSquare(slow)
            fast = self.getSquare(self.getSquare(fast))
            if slow == fast:
                break
        return slow == 1

    def getSquare(self, n):
        _sum = 0
        while n > 0:
            digit = n % 10
            _sum += digit * digit
            n //= 10
        return _sum


'''
Time: O(logn)
'''
